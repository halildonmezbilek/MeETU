from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, Runnable
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv
import streamlit as st
import asyncio


load_dotenv()

embedding_model_name = "all-MiniLM-L6-v2"
faiss_local_dir = f"vectordatabase/faiss_index_{embedding_model_name}"
chunk_size_of_embeddings = 500
llm_model_name = "meta-llama/Llama-3.2-3B-Instruct"
top_k=5


#################### Embedding Model Setup ####################

@st.cache_resource
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name=embedding_model_name)

embedding_model = get_embedding_model()
vector_store = FAISS.load_local(
    faiss_local_dir, embedding_model, allow_dangerous_deserialization=True
)

#################### HuggingFace LLM ####################

#@st.cache_resource
llm = HuggingFaceEndpoint(
    repo_id=llm_model_name,
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN"),
    max_new_tokens=3500-chunk_size_of_embeddings,
    temperature=0.1
)

###########################################################

retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": top_k})

#################### Prompt Template ####################

template = """
You are an advanced AI assistant for prospective students of Middle East Technical University (METU), designed to provide accurate, helpful, and detailed information.
Your role is to answer students' questions about METU's programs, campus life, application processes, facilities, and any other general information.
Use a friendly and approachable tone, and whenever possible, include details that would help students make an informed decision.
You will respond the user's language.

User:
{question}


Context:
{context}


Answer:
"""

prompt = ChatPromptTemplate.from_template(template) 


#################### Helper Functions ####################

def format_docs(docs):
    if not docs:
        return "No relevant context found."
    return "\n\n".join([doc.page_content for doc in docs])


#################### RAG Chain Setup ####################

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | {"response": StrOutputParser(), "contexts": retriever }
)

rag_chain_tru = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
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
