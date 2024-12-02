import sys
import os
import time
import signal
from dotenv import load_dotenv
import warnings
import pandas as pd

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

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rag_model import rag_chain

warnings.filterwarnings("ignore")
load_dotenv()

warnings.filterwarnings("ignore")
load_dotenv()

def meetu_evaluate_metrics(
                test_data_path: str = "/home/halil/Desktop/MeETU/RAG_Model/ragasio/controlled_test_data.pkl",
                openai_api_key: str = None,
                demo: bool = False,
                rag_chain=rag_chain,
            ) -> tuple:
    """
    Evaluates the metrics on the provided test dataset.

    Parameters:
    test_data_path (str): Path to the test dataset file. Default is '/home/halil/Desktop/MeETU/RAG_Model/ragasio/controlled_test_data.pkl'.
    openai_api_key (str): OpenAI API key for accessing the model.

    Returns:
    tuple: Contains `results`, `results_df`, and `results_df_metrics_stats`.
    """
    rag_chain= rag_chain
    def generate_chain_output(question, rag_chain=rag_chain):
        chain_output = rag_chain.invoke(question)
        return chain_output["response"], chain_output["contexts"]
    
    test_data = pd.read_pickle(test_data_path)

    # def timeout_handler(signum, frame):
    #     raise TimeoutError("Operation timed out")

    # def get_response_for_test_data_with_retry(row, retries=3, timeout=800):
    #     """
    #     Synchronously wraps `generate_chain_output` with timeout and retry logic.
    #     Measures the latency of `generate_chain_output(row)`.
        
    #     Parameters:
    #     - row: The data row to process.
    #     - retries: Number of retry attempts.
    #     - timeout: Timeout duration for each attempt in seconds.
        
    #     Returns:
    #     - response: The generated response.
    #     - context: The retrieved context.
    #     - latency: Time taken for the `generate_chain_output` call.
    #     """
    #     for attempt in range(retries):
    #         try:
    #             start_time = time.time()
    #             response, context = generate_chain_output(row)
    #             end_time = time.time()
                
    #             # Ensure that the function hasn't exceeded the timeout
    #             elapsed_time = end_time - start_time
    #             if elapsed_time > timeout:
    #                 raise TimeoutError(f"Timeout exceeded: {elapsed_time} > {timeout}")
                
    #             context = [doc.page_content for doc in context]
    #             latency = end_time - start_time
    #             return response, context, latency
    #         except TimeoutError:
    #             print(f"Attempt {attempt + 1} timed out, retrying...")
    #             if attempt < retries - 1:
    #                 time.sleep(2)
    #             else:
    #                 raise TimeoutError("Max retry attempts reached, operation failed.")
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    #             raise

    def meetu_generate_response(row):
        start_time = time.time()
        response, context = generate_chain_output(row)
        end_time = time.time()
        context = [doc.page_content for doc in context]
        latency = end_time - start_time
        return response, context, latency

    
    if demo != False:
        test_data = test_data.head()

    #test_data["response"], test_data["retrieved_contexts"], test_data["latency"] = zip(*test_data["user_input"].apply(lambda row: get_response_for_test_data_with_retry(row)))

    test_data["response"], test_data["retrieved_contexts"], test_data["latency"] = zip(*test_data["user_input"].apply(meetu_generate_response))
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
        # Context Relevance
        LLMContextRecall(llm=evaluator_llm), 
        NonLLMContextPrecisionWithReference(),

        # Faithfulness
        FactualCorrectness(llm=evaluator_llm), 
        Faithfulness(llm=evaluator_llm),

        # Answer Relevance
        SemanticSimilarity(embeddings=evaluator_embeddings),
    ]

    # def evaluate_with_retry(eval_dataset, metrics, retries=3, timeout=800):
    #     """
    #     Wraps the evaluate() function with timeout and retry logic.

    #     Parameters:
    #     - eval_dataset: The EvaluationDataset.
    #     - metrics: List of metrics to evaluate.
    #     - retries: Number of retry attempts.
    #     - timeout: Timeout duration for each attempt in seconds.

    #     Returns:
    #     - results: The evaluation results.
    #     """
    #     for attempt in range(retries):
    #         try:
    #             signal.signal(signal.SIGALRM, timeout_handler)
    #             signal.alarm(timeout)
    #             results = evaluate(dataset=eval_dataset, metrics=metrics)
    #             signal.alarm(0)
    #             return results
    #         except TimeoutError:
    #             print(f"Attempt {attempt + 1} to evaluate() timed out, retrying...")
    #             if attempt < retries - 1:
    #                 time.sleep(2)
    #             else:
    #                 signal.alarm(0)
    #                 raise TimeoutError("Max retry attempts reached, operation failed.")
    #         except Exception as e:
    #             signal.alarm(0)
    #             print(f"An error occurred during evaluation: {e}")
    #             raise

    # results = evaluate_with_retry(eval_dataset, metrics)

    results = evaluate(dataset=eval_dataset, metrics=metrics)

    results_df = results.to_pandas()

    results_df_metrics_stats = results_df[['context_recall',
                                           'non_llm_context_precision_with_reference', 
                                           'factual_correctness',
                                           'faithfulness', 
                                           'semantic_similarity']].describe()

    return results, results_df, results_df_metrics_stats, average_latency
