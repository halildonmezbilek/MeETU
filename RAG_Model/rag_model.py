import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS

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
    def __init__(self, retriever, prompt_template, llm):
        self.retriever = retriever
        self.prompt_template = prompt_template
        self.llm = llm
        self.chain = self._build_chain()

    def _build_chain(self):
        """Builds the RAG chain."""
        return (
            {
                "context": self.retriever | self.format_docs,
                "question": RunnablePassthrough()
            }
            | self.prompt_template
            | self.llm
            | {"response": StrOutputParser(), "contexts": self.retriever}
        )

    @staticmethod
    def format_docs(docs):
        """Formats documents into a string."""
        if not docs:
            return "No relevant context found."
        return "\n\n".join([doc.page_content for doc in docs])

    def invoke(self, question):
        """Invokes the RAG chain synchronously."""
        return self.chain.invoke(question)

    async def async_invoke(self, question):
        """Invokes the RAG chain asynchronously."""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self.chain.invoke, question)

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

    This class integrates a retriever (for fetching relevant context from a vector store of embeddings) 
    and a language model (for generating coherent, context-aware responses). It can be used both 
    as a Streamlit app component or as a standalone backend.

    Attributes:
        isstreamlitapp (bool): Indicates whether the assistant is running within a Streamlit app.
        embedding_model_name (str): The name of the embedding model to use for vector representation of documents.
        vectorstore_dir (str): Directory path to the stored FAISS vector database.
        llm_repo_id (str): The repository ID for the Hugging Face language model.
        llm_api_token (str): The API token used to authenticate with the Hugging Face model endpoint.
        max_new_tokens (int): The maximum number of tokens the language model can generate.
        search_type (str): The type of retrieval method to use (e.g., "mmr").
        top_k (int): The number of top results to retrieve from the vector store.
        temperature (float): The temperature parameter for the language model to control the 
                             randomness of the output.

    Methods:
        generate_response(question: str) -> str:
            Generates a response synchronously to the given user question based on retrieved context 
            and the language model's completion.

        agenerate_response(question: str) -> str:
            An asynchronous version of the response generation method, useful for non-blocking I/O 
            operations or when integrating into async frameworks.

    Example:
        meetu_assistant = MeETUAssistant(
            isstreamlitapp=False,
            embedding_model_name="all-MiniLM-L6-v2",
            vectorstore_dir="path/to/vectordb",
            llm_repo_id="meta-llama/Llama-3.2-3B-Instruct",
            llm_api_token="your_hf_api_token",
            max_new_tokens=3500,
            search_type="mmr",
            top_k=5,
            temperature=0.3
        )
        response = meetu_assistant.generate_response("Can you tell me about dormitories at METU?")
        print(response)

    Notes:
        - Ensure that the provided vector store directory and embedding model are compatible.
        - The Hugging Face endpoint should be accessible with the given API token.
        - Adjust parameters such as `temperature` and `top_k` to tune the retrieval and generation results.
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

        # Initialize RAG chain
        self.prompt_template = ChatPromptTemplate.from_template(self._get_prompt_template())
        self.rag_chain_manager = RAGChainManager(self.retriever, self.prompt_template, self.llm)

    @staticmethod
    def _get_prompt_template():
        return """
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

    def generate_response(self, question):
        """Generates a response synchronously."""
        chain_output = self.rag_chain_manager.invoke(question)
        return chain_output["response"]

    async def agenerate_response(self, question):
        """Generates a response asynchronously."""
        chain_output = await self.rag_chain_manager.async_invoke(question)
        return chain_output["response"]


# embedding_model_name = "all-MiniLM-L6-v2"
# faiss_local_dir = f"vectordatabase/faiss_index_{embedding_model_name}"
# llm_model_name = "meta-llama/Llama-3.2-3B-Instruct"
# top_k = 5
# search_type = "mmr"
# temperature = 0.3
# max_new_tokens = 3500
# llm_api_token = os.getenv("HUGGINGFACE_API_TOKEN")

# meetu_assistant = MeETUAssistant(
#     True, embedding_model_name, faiss_local_dir, llm_model_name, llm_api_token, max_new_tokens, search_type, top_k, temperature
# )

# print(meetu_assistant.generate_response("How can I connect wifi?"))