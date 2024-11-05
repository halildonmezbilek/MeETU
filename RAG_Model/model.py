import os
import time
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
from llama_cpp import Llama
from langchain import PromptTemplate
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

from bert_score import score as bert_score
from rouge_score import rouge_scorer

load_dotenv()

class ChromaDBRetriever:
    def __init__(self, chroma_collection, embedding_model):
        self.collection = chroma_collection
        self.embedding_model = embedding_model

    def get_relevant_documents(self, query_text):
        query_embedding = self.embedding_model.encode(query_text)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=1
        )
        documents = []
        for i in range(len(results['metadatas'][0])):
            doc_id = results['ids'][0][i] if 'ids' in results and results['ids'][0] else None
            metadata = results['metadatas'][0][i] if results['metadatas'][0][i] else {}
            document_content = results['documents'][0][i] if 'documents' in results and results['documents'][0] else 'No content available'
            
            documents.append({
                'id': doc_id,
                'content': document_content,
                'metadata': metadata
            })
            
        return documents
    
class LlamaWrapper:
    def __init__(self, model, max_tokens=290): # Max token size 512
        self.model = model
        self.max_tokens = max_tokens

    def __call__(self, prompt, stream=False):
        truncated_prompt = self._truncate_prompt(prompt)
        available_tokens_for_response = self.max_tokens - self._count_tokens(truncated_prompt)

        return self.model.create_chat_completion(
            messages=[{"role": "user", "content": truncated_prompt}],
            stream=stream,
            max_tokens=available_tokens_for_response
        )

    def _count_tokens(self, text):
        return len(text.split())

    def _truncate_prompt(self, prompt):
        tokens = prompt.split()
        if len(tokens) > self.max_tokens:
            return " ".join(tokens[:self.max_tokens])
        return prompt


prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
        "You are an advanced AI assistant for prospective students of Middle East Technical University (METU), designed to provide accurate, helpful, and detailed information. "
        "Your role is to answer students' questions about METU's programs, campus life, application processes, facilities, and any other general information. "
        "Use a friendly and approachable tone, and whenever possible, include details that would help students make an informed decision.\n\n"
        "{context}\n<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        "{question}\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )
)

def initialize_components():
    client = chromadb.HttpClient(
        host="localhost",
        port=6854,
        settings=Settings(
            chroma_client_auth_provider="chromadb.auth.basic_authn.BasicAuthClientProvider",
            chroma_client_auth_credentials=os.getenv("CHROMA_CLIENT_AUTH_CREDENTIALS")
        )
    )

    collection = client.get_collection("faq_embeddings")
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    retriever = ChromaDBRetriever(collection, embedding_model)

    llm = Llama.from_pretrained(
        repo_id="bartowski/Meta-Llama-3.1-8B-Instruct-GGUF",
        filename="Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf",
        local_dir="models"
    )
    wrapped_llm = LlamaWrapper(llm)


    return retriever, wrapped_llm


def generate_response(retriever, wrapped_llm, question):
    relevant_docs = retriever.get_relevant_documents(question)
    context = " ".join([doc['content'] for doc in relevant_docs])
    prompt = prompt_template.format(context=context, question=question)
    response = wrapped_llm(prompt)
    response_content = response['choices'][0]['message']['content']
    return response_content

rouge_scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

def evaluate_performance(retriever, wrapped_llm, synthetic_question, ground_truth_answer, ground_truth_id):

    query_results = retriever.get_relevant_documents(synthetic_question)
    if query_results and 'id' in query_results[0]:
        top_doc_id = query_results[0]['id']
    else:
        top_doc_id = None

    precision_at_1 = 1 if int(top_doc_id) == ground_truth_id else 0

    context = " ".join([doc['content'] for doc in query_results])
    prompt = prompt_template.format(context=context, question=synthetic_question)

    start_time = time.time()
    generated_response = wrapped_llm(prompt)
    response_time = time.time() - start_time

    response_text = generated_response['choices'][0]['message']['content'] if isinstance(generated_response, dict) else str(generated_response)

    P, R, F1 = bert_score([response_text], [ground_truth_answer], lang="en")
    bert_score_value = F1[0].item()

    rouge_l_score = rouge_scorer.score(response_text, ground_truth_answer)['rougeL'].fmeasure

    return {
        "generated_response": response_text,
        "response_time": response_time,
        "precision_at_1": precision_at_1,
        "bert_score": bert_score_value,
        "rouge_l_score": rouge_l_score
    }
