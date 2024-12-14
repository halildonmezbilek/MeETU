import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableMap, RunnableLambda
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS

from langdetect import detect

load_dotenv()

class EmbeddingModelManager:
    """Manages the embedding model setup."""
    def __init__(self, model_name, vectorstore_dir):
        self.model_name = model_name
        self.vectorstore_dir = vectorstore_dir

    def get_embedding_model(self):
        """Loads the Hugging Face embedding model."""
        return HuggingFaceEmbeddings(model_name=self.model_name)

    def load_vector_store(self):
        """Loads the FAISS vector store."""
        embedding_model = self.get_embedding_model()
        return FAISS.load_local(
            self.vectorstore_dir, embedding_model, allow_dangerous_deserialization=True
        )

class HuggingFaceLLMManager:
    """Manages the Hugging Face language model."""
    def __init__(self, repo_id, api_token, max_new_tokens, temperature=0.7):
        self.repo_id = repo_id
        self.api_token = api_token
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature

    def get_llm(self):
        """Returns a Hugging Face Endpoint LLM."""
        return HuggingFaceEndpoint(
            repo_id=self.repo_id,
            huggingfacehub_api_token=self.api_token,
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature
        )


class RAGChainManager:
    """Manages the RAG chain setup and query execution."""
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

        # English and Turkish templates
        self.english_template = """
        You are an advanced AI assistant for prospective students of Middle East Technical University (METU), designed to provide accurate, helpful, and detailed information.
        Answer the user's question as concisely as possible while retaining essential details. If the context is long, prioritize the most relevant parts for the answer.
        Maintain a friendly and approachable tone.

        User:
        {question}

        Context:
        {context}

        Answer:
        """

        self.turkish_template = """
        Sen Orta Doğu Teknik Üniversitesi (ODTÜ) için potansiyel öğrencilere doğru, faydalı ve detaylı bilgi sağlamak üzere tasarlanmış ileri bir AI asistansın.
        Kullanıcının sorusuna mümkün olduğunca kısa ancak gerekli detayları içerecek şekilde Türkçe cevap ver. 
        Eğer bağlamda yer alan belgeler İngilizce ise, önce bu bilgileri Türkçeye özetleyerek aktar.
        Eğer bağlam uzunsa, cevaba en uygun kısımlara öncelik verin.
        Samimi ve ulaşılabilir bir ton kullanın.

        Kullanıcı:
        {question}

        Bağlam (İngilizce kaynaklar olabilir, gerekli bilgiyi Türkçeye çevir ve özetle):
        {context}

        Cevap:
        """

    @staticmethod
    def format_docs(docs):
        """Formats documents into a string."""
        if not docs:
            return "No relevant context found."
        return "\n\n".join([doc.page_content for doc in docs])

    def get_prompt_template(self, question):
        """Selects the prompt template based on the question's language."""
        lang = detect(question)
        if lang == "tr":
            return ChatPromptTemplate.from_template(self.turkish_template)
        else:
            return ChatPromptTemplate.from_template(self.english_template)

    def build_chain(self, question):
        """Builds the chain dynamically for each question."""

        def print_and_return_prompt(inputs):
            prompt = self.get_prompt_template(inputs["question"]).format(
                question=inputs["question"],
                context=inputs["context"]
            )
            # print("PROMPT:", prompt)
            return prompt

        return (
            RunnableMap({
                "context": self.retriever | self.format_docs,
                "question": RunnablePassthrough()
            })
            | RunnableLambda(print_and_return_prompt)
            | self.llm
            | RunnableMap({
                "response": StrOutputParser(),
                "contexts": self.retriever
            })
        )

    def invoke(self, question):
        """Invokes the RAG chain synchronously."""
        chain = self.build_chain(question)
        return chain.invoke(question)

    async def async_invoke(self, question):
        """Invokes the RAG chain asynchronously."""
        loop = asyncio.get_running_loop()
        chain = self.build_chain(question)
        return await loop.run_in_executor(None, chain.invoke, question)

def cached_instance(cls):
    @st.cache_resource
    def wrapper(*args, **kwargs):
        return cls(*args, **kwargs)
    return wrapper

embeddingmodelmanager_cached = cached_instance(EmbeddingModelManager)
huggingfacellmmanager_cached = cached_instance(HuggingFaceLLMManager)

class MeETUAssistant:
    """
    MeETUAssistant is a RAG (Retrieval-Augmented Generation) based AI assistant designed to help prospective 
    students of Middle East Technical University (METU) with information about programs, campus life, 
    application processes, facilities, and other general inquiries about METU.
    """

    def __init__(self, isstreamlitapp, embedding_model_name, vectorstore_dir, llm_repo_id, llm_api_token, max_new_tokens, search_type="mmr", top_k=5, temperature=0.2):
        # Initialize embedding model and vector store
        if isstreamlitapp:
            self.embedding_manager = embeddingmodelmanager_cached(embedding_model_name, vectorstore_dir)
        else:
            self.embedding_manager = EmbeddingModelManager(embedding_model_name, vectorstore_dir)
        self.vector_store = self.embedding_manager.load_vector_store()
        self.retriever = self.vector_store.as_retriever(search_type=search_type, search_kwargs={"k": top_k})

        # Initialize LLM
        if isstreamlitapp:
            self.llm_manager = huggingfacellmmanager_cached(llm_repo_id, llm_api_token, max_new_tokens, temperature)
        else:
            self.llm_manager = HuggingFaceLLMManager(llm_repo_id, llm_api_token, max_new_tokens, temperature)
        self.llm = self.llm_manager.get_llm()

        # Initialize RAG chain manager with language selection logic
        self.rag_chain_manager = RAGChainManager(self.retriever, self.llm)

    def generate_response(self, question):
        """Generates a response synchronously."""
        chain_output = self.rag_chain_manager.invoke(question)
        return chain_output["response"]

    async def agenerate_response(self, question):
        """Generates a response asynchronously."""
        chain_output = await self.rag_chain_manager.async_invoke(question)
        return chain_output["response"]


# embedding_model_name = "paraphrase-multilingual-MiniLM-L12-v2"
# faiss_local_dir = f"vectordatabase/faiss_index_{embedding_model_name}"
# llm_model_name = "mistralai/Mistral-7B-Instruct-v0.3"
# top_k = 7
# search_type = "similarity"
# temperature = 0.3
# max_new_tokens = 3500
# llm_api_token = os.getenv("HUGGINGFACE_API_TOKEN")

# meetu_assistant = MeETUAssistant(
#     False, embedding_model_name, faiss_local_dir, llm_model_name, llm_api_token, max_new_tokens, search_type, top_k, temperature
# )

# print(meetu_assistant.generate_response("futbol oynamayı çok seviyorum hangi öğrenci klüplerini önerirsin?"))