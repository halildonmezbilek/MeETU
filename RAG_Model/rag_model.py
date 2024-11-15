from langchain.prompts import PromptTemplate
from langchain_chroma.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, Runnable
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import InferenceClient
import chromadb
from chromadb.config import Settings
import os
from dotenv import load_dotenv
import streamlit as st
import asyncio


load_dotenv()

#################### ChromaDB and Embedding Model Setup ####################

@st.cache_resource
def get_chroma_client():
    return chromadb.HttpClient(
        host="localhost",
        port=6854,
        settings=Settings(
            chroma_client_auth_provider="chromadb.auth.basic_authn.BasicAuthClientProvider",
            chroma_client_auth_credentials=os.getenv("CHROMA_CLIENT_AUTH_CREDENTIALS")
        )
    )

@st.cache_resource
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

@st.cache_resource
def get_vector_store(_client, _embedding_model):
    return Chroma(
        collection_name="MeETUVectorDB_Chunks",
        embedding_function=_embedding_model,
        persist_directory="/home/halil/Desktop/MeETU/RAG_Model/chroma_db",
        client=_client
    )

@st.cache_resource
def get_ollama_llm():
    return OllamaLLM(
        model="hf.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:Q6_K",
        temperature=0.1,
        base_url="http://localhost:11434"
    )

#################### Custom Runnable for Hugging Face ####################

@st.cache_resource
def get_huggingface_llm():
    hf_api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    return InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=hf_api_token)

class HuggingFaceChatCompletionRunnable(Runnable):
    def __init__(self, inference_client):
        self.inference_client = inference_client

    def invoke(self, question, config=None):
        if hasattr(question, "to_string"):
            question = question.to_string()
        messages = [{"role": "user", "content": question}]
        response = self.inference_client.chat_completion(messages, max_tokens=8000)
        return response["choices"][0]["message"]["content"]

###########################################################

@st.cache_resource
def get_local_huggingface_llm():
    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
    model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
    return model, tokenizer

class LocalHuggingFaceLLMRunnable(Runnable):
    def __init__(self, model, tokenizer):
        self.model = model.to("cuda")
        self.tokenizer = tokenizer  

    def invoke(self, question, config=None):
        inputs = self.tokenizer(question, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=8000, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
###########################################################

client = get_chroma_client()
embedding_model = get_embedding_model()
vector_store = get_vector_store(_client=client, _embedding_model=embedding_model)
retriever = vector_store.as_retriever(search_type="similarity", 
                                      search_kwargs={"k": 7})
def select_llm(model_type=None):
    if model_type == "Ollama":
        return get_ollama_llm()
    elif model_type == "HuggingFace":
        return HuggingFaceChatCompletionRunnable(get_huggingface_llm())
    elif model_type == "LocalHuggingFace":
        model, tokenizer = get_local_huggingface_llm()
        return LocalHuggingFaceLLMRunnable(model, tokenizer)

llm = select_llm("HuggingFace")

#################### Prompt Template ####################
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "You are an advanced AI assistant for prospective students of Middle East Technical University (METU), designed to provide accurate, helpful, and detailed information. "
        "Your role is to answer students' questions about METU's programs, campus life, application processes, facilities, and any other general information. "
        "Use a friendly and approachable tone, and whenever possible, include details that would help students make an informed decision. "
        "{context}\n\nUser: {question}\nAssistant:"
    )
)

#################### Helper Functions ####################

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

#################### RAG Chain Setup ####################

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt_template
    | llm
    | {"response": StrOutputParser(), "contexts": retriever }
)

#################### Generate Response Using RAG Chain ####################
def generate_response(question):
    chain_output = rag_chain.invoke(question)
    return chain_output["response"]

async def agenerate_response(question):
    loop = asyncio.get_running_loop()
    chain_output = await loop.run_in_executor(None, rag_chain.invoke, question)
    return chain_output["response"]

async def agenerate_chain_output(question):
    loop = asyncio.get_running_loop()
    chain_output = await loop.run_in_executor(None, rag_chain.invoke, question)
    return chain_output

