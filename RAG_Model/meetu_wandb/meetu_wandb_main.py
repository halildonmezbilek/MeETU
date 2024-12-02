import os
import wandb
import json
import itertools

from meetu_test_eval import meetu_evaluate_metrics
from langchain_community.document_loaders import UnstructuredExcelLoader, UnstructuredMarkdownLoader
from langchain_huggingface import HuggingFaceEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from uuid import uuid4
from langchain_core.documents import Document
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pandas as pd

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

sweep_config = {
    'method': 'grid',
    'parameters': {
        'embed_model_name': {
            'values': ['all-MiniLM-L6-v2']
        },
        'chunk_size': {
            'values': [500, 700]
        },
        'chunk_overlap': {
            'values': [50, 100]
        },
        'llm_model_name': {
            'values': ['meta-llama/Llama-3.2-3B-Instruct', "mistralai/Mistral-7B-Instruct-v0.3"]
        },
        'top_k': {
            'values': [5]
        },
    }
}

keys, values = zip(*sweep_config.items())

hyperparameter_combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]



def sweep_fn():
    with wandb.init() as run:
        config = wandb.config

        embed_model_name = config.embed_model_name
        chunk_size = config.chunk_size
        chunk_overlap = config.chunk_overlap
        llm_model_name = config.llm_model_name
        top_k = config.top_k

        vector_store_main_foder = Path("/home/halil/Desktop/MeETU/RAG_Model/vectordatabase")
        data_folder = Path("data")
        files = [
            "accomadation.xlsx", "courses.xlsx", "extras.xlsx", "faq.xlsx",
            "fees_and_scholarships.md", "how_to_register.xlsx", "registration_procedures.xlsx",
            "sports_club.xlsx", "student_club.xlsx"
        ]

        docs = []
        for file in files:
            file_path = vector_store_main_foder / data_folder / file
            if file.endswith('.xlsx'):
                loader = UnstructuredExcelLoader(str(file_path), mode="elements")
            elif file.endswith('.md'):
                loader = UnstructuredMarkdownLoader(str(file_path))
            else:
                print(f"Unsupported file type: {file}")
                continue
            try:
                doc = loader.load()
                docs.extend(doc)
            except Exception as e:
                print(f"Error loading {file}: {e}")

        embeddings = HuggingFaceEmbeddings(model_name=embed_model_name)

        _doc_texts = [doc.page_content for doc in docs if hasattr(doc, 'page_content')]
        doc_texts = [text for text in _doc_texts if text != "Context"]

        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunked_texts = [chunk for text in doc_texts for chunk in splitter.split_text(text)]
        doc_embeddings = embeddings.embed_documents(chunked_texts)

        index = faiss.IndexFlatL2(len(doc_embeddings[0]))

        vector_store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )

        documents = [Document(page_content=text) for text in chunked_texts]
        uuids = [str(uuid4()) for _ in range(len(documents))]
        vector_store.add_documents(documents=documents, ids=uuids)

        print(f"FAISS vector store created with {len(documents)} documents.")

        faiss_local_dir = vector_store_main_foder / f"faiss_index_{embed_model_name}-{chunk_size}-{chunk_overlap}"
        vector_store.save_local(faiss_local_dir)

        def get_embedding_model():
            return HuggingFaceEmbeddings(model_name=embed_model_name)

        embedding_model = get_embedding_model()
        vector_store = FAISS.load_local(
            faiss_local_dir, embedding_model, allow_dangerous_deserialization=True
        )

        llm = HuggingFaceEndpoint(
            repo_id=llm_model_name,
            huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN"),
            max_new_tokens=3500 - chunk_size,
            temperature=0.1
        )

        retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": top_k})

        template = """
        You are an advanced AI assistant for prospective students of Middle East Technical University (METU), designed to provide accurate, helpful, and detailed information.
        Your role is to answer students' questions about METU's programs, campus life, application processes, facilities, and any other general information.
        Use a friendly and approachable tone, and whenever possible, include details that would help students make an informed decision.

        User:
        {question}


        Context:
        {context}


        Answer:
        """

        prompt = ChatPromptTemplate.from_template(template)

        def format_docs(docs):
            if not docs:
                return "No relevant context found."
            return "\n\n".join([doc.page_content for doc in docs])

        rag_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | {"response": StrOutputParser(), "contexts": retriever }
        )

        results, results_df, results_df_metrics_stats, average_latency = meetu_evaluate_metrics(
            openai_api_key=os.getenv("OPEN_AI"), rag_chain=rag_chain
        )

        wandb.log({
            'average_latency': average_latency,
            'metrics_stats': results_df_metrics_stats.to_dict(),
        })

        artifact = wandb.Artifact('evaluation_results', type='dataset')

        results_df_csv = 'results_df.csv'
        results_df.to_csv(results_df_csv, index=False)
        artifact.add_file(results_df_csv)

        run.log_artifact(artifact)

sweep_id = wandb.sweep(sweep_config, project='MeETU')

wandb.agent(sweep_id, function=sweep_fn)