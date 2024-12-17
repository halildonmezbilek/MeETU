import asyncio
import os
import time
import json
import itertools
import pandas as pd
import warnings
from uuid import uuid4
from pathlib import Path
from dotenv import load_dotenv
import wandb
import faiss

from ragas.metrics import (
    LLMContextRecall,
    Faithfulness,
    FactualCorrectness,
    SemanticSimilarity,
    NonLLMContextPrecisionWithReference,
)
from ragas import evaluate, EvaluationDataset
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_community.document_loaders import UnstructuredExcelLoader, UnstructuredMarkdownLoader
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableMap, RunnableLambda

from huggingface_hub.errors import InferenceTimeoutError

from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from langdetect import detect

from tqdm.asyncio import tqdm_asyncio

warnings.filterwarnings("ignore")
load_dotenv()

sweep_config = {
    'method': 'bayes',
    'metric': {
        'name': 'rag_triad_mean',
        'goal': 'maximize'
    },
    'parameters': {
        'embed_model_name': {
            'values': ['all-MiniLM-L6-v2', 'all-MiniLM-L12-v2']
        },
        'chunk_size': {
            'values': [200, 500, 1000, 1500, 2000]
        },
        'chunk_overlap': {
            'values': [50, 100, 150, 200, 250, 300]
        },
        'llm_model_name': {
            'values': ["mistralai/Mistral-7B-Instruct-v0.3"] 
        },
        'top_k': {
            'values': [3, 5, 7, 10]
        },
        'search_type': {
            'values': ["mmr", "similarity"] 
        },
        'temperature': {
            'values': [0.3, 0.5, 0.7]
        },
    }
}

keys, values = zip(*sweep_config.items())
hyperparameter_combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

async def agenerate_chain_output(question, rag_chain):
    chain_output = await rag_chain.ainvoke(question)
    return chain_output["response"], chain_output["contexts"]

@retry(stop=stop_after_attempt(3), wait=wait_fixed(60), retry=retry_if_exception_type(InferenceTimeoutError))
async def meetu_generate_response_async(row, rag_chain):
    start_time = time.time()
    response, context = await agenerate_chain_output(row, rag_chain)
    end_time = time.time()
    context = [doc.page_content for doc in context]
    latency = end_time - start_time
    #print(latency)
    return response, context, latency

async def process_test_data_async(test_data, rag_chain):
    tasks = [meetu_generate_response_async(row, rag_chain) for row in test_data["user_input"]]
    # results = await asyncio.gather(*tasks)
    results = await tqdm_asyncio.gather(*tasks)
    return results

async def meetu_evaluate_metrics(
    test_data_path: str,
    openai_api_key: str = None,
    demo: bool = False,
    rag_chain=None,
):
    test_data = pd.read_pickle(test_data_path)

    if demo:
        test_data = test_data.head()

    results = await process_test_data_async(test_data, rag_chain)

    test_data["response"], test_data["retrieved_contexts"], test_data["latency"] = zip(*results)
    average_latency = test_data["latency"].mean()

    test_data = test_data[['user_input', 'reference', 'reference_contexts', 'response', 'retrieved_contexts']]

    eval_dataset = EvaluationDataset.from_pandas(test_data)

    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    else:
        raise ValueError("OpenAI API key is required.")

    evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
    evaluator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

    metrics = [
        LLMContextRecall(llm=evaluator_llm),
        NonLLMContextPrecisionWithReference(),
        FactualCorrectness(llm=evaluator_llm),
        Faithfulness(llm=evaluator_llm),
        SemanticSimilarity(embeddings=evaluator_embeddings),
    ]

    print("Ragas evaluation started...")
    results = evaluate(dataset=eval_dataset, metrics=metrics)

    results_df = results.to_pandas()

    results_df_metrics_stats = results_df[['context_recall',
                                           'non_llm_context_precision_with_reference',
                                           'factual_correctness',
                                           'faithfulness',
                                           'semantic_similarity']].describe()
    results_df_metrics_stats = results_df_metrics_stats.reset_index()
    results_df_metrics_stats.rename(columns={'index': 'statistic'}, inplace=True)

    return results, results_df, results_df_metrics_stats, average_latency


async def sweep_fn_async():
    with wandb.init() as run:
        config = wandb.config

        embed_model_name = config.embed_model_name
        chunk_size = config.chunk_size
        chunk_overlap = config.chunk_overlap
        llm_model_name = config.llm_model_name
        top_k = config.top_k
        search_type = config.search_type
        temperature = config.temperature

        vector_store_main_folder = Path("/home/halil/Desktop/MeETU/RAG_Model/vectordatabase")
        faiss_local_dir = vector_store_main_folder / f"faiss_index_{embed_model_name}-{chunk_size}-{chunk_overlap}-{search_type}-{top_k}"

        if faiss_local_dir.exists():
            print(f"FAISS vector store already exists at {faiss_local_dir}.")
        else:
            data_folder = Path("data")
            files = [
                "accomadation.xlsx", "courses.xlsx", "extras.xlsx", "faq.xlsx",
                "fees_and_scholarships.md", "how_to_register.xlsx", "registration_procedures.xlsx",
                "sports_club.xlsx", "student_club.xlsx"
            ]

            docs = []
            for file in files:
                file_path = vector_store_main_folder / data_folder / file
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

            vector_store.save_local(faiss_local_dir)
            time.sleep(30)

        def get_embedding_model():
            return HuggingFaceEmbeddings(model_name=embed_model_name)

        embedding_model = get_embedding_model()
        vector_store = FAISS.load_local(
            faiss_local_dir, embedding_model, allow_dangerous_deserialization=True
        )

        llm = HuggingFaceEndpoint(
            repo_id=llm_model_name,
            huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN"),
            max_new_tokens=3000,
            temperature=temperature,
            timeout=240
        )

        retriever = vector_store.as_retriever(search_type=search_type, search_kwargs={"k": top_k})

        english_template = """
        You are an advanced AI assistant for prospective students of Middle East Technical University (METU), designed to provide accurate, helpful, and detailed information.
        Answer the user's question as concisely as possible while retaining essential details. If the context is long, prioritize the most relevant parts for the answer.
        Maintain a friendly and approachable tone.

        User:
        {question}


        Context:
        {context}


        Answer:
        """

        turkish_template = """
        Sen Orta Doğu Teknik Üniversitesi (ODTÜ) için potansiyel öğrencilere doğru, faydalı ve detaylı bilgi sağlamak üzere tasarlanmış ileri bir AI asistansın.
        Kullanıcının sorusuna mümkün olduğunca kısa ancak gerekli detayları içerecek şekilde cevap veriyorsun. Eğer içerik uzunsa, cevaba en uygun kısımlara öncelik verin.
        Samimi ve ulaşılabilir bir ton kullanın. 

        Kullanıcı:
        {question}


        Bağlam:
        {context}


        Cevap:
        """

        def format_docs(docs):
            if not docs:
                return "No relevant context found."
            return "\n\n".join([doc.page_content for doc in docs])

        def get_prompt_template(question):
            lang = detect(question)
            if lang == "tr":
                return ChatPromptTemplate.from_template(turkish_template)
            else:
                return ChatPromptTemplate.from_template(english_template)

        rag_chain = (
                    RunnableMap({
                        "context": retriever | format_docs,
                        "question": RunnablePassthrough()
                    })

                    | RunnableLambda(
                        lambda inputs: get_prompt_template(inputs["question"]).format(
                            question=inputs["question"],
                            context=inputs["context"]
                        )
                    )
                    | llm 

                    | RunnableMap({
                        "response": StrOutputParser(),
                        "contexts": retriever
                    })
                )

        print("Evaluating...")
        results, results_df, results_df_metrics_stats, average_latency = await meetu_evaluate_metrics(
            test_data_path="/home/halil/Desktop/MeETU/RAG_Model/ragasio/final_test_data_set.pkl",
            openai_api_key=os.getenv("OPEN_AI"),
            rag_chain=rag_chain,
            demo=False
        )

        wandb.log({
            'average_latency': average_latency,
            'metrics_stats': results_df_metrics_stats.to_dict(),
        })


        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        safe_llm_model_name = llm_model_name.replace("/", "_")
        results_df_csv = results_dir / f'results_df-{embed_model_name}-{chunk_size}-{chunk_overlap}-{safe_llm_model_name}-{top_k}-{search_type}-{temperature}.csv'
        results_df.to_csv(results_df_csv, index=False)

        results_wandb = wandb.Table(dataframe=results_df)
        results_wandb_stats = wandb.Table(dataframe=results_df_metrics_stats)

        wandb.log({"results_table": results_wandb,
                   "results_metric_stats_table":results_wandb_stats })
        artifact = wandb.Artifact("results_artifact", type="dataset")
        artifact.add_file(str(results_df_csv))
        run.log_artifact(artifact)

        mean_values = results_df_metrics_stats[results_df_metrics_stats['statistic'] == 'mean']
        selected_metrics = ['context_recall', 'factual_correctness', 'semantic_similarity']
        rag_triad_mean = mean_values[selected_metrics].mean(axis=1).values[0]
        wandb.log({
            'rag_triad_mean': rag_triad_mean,
        })

        await asyncio.sleep(60)


def sweep_fn():
    return loop.run_until_complete(sweep_fn_async())

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    sweep_id = wandb.sweep(sweep_config, project='MeETU_Experiment3')
    wandb.agent(sweep_id, function=sweep_fn, count=10)

    loop.close()
