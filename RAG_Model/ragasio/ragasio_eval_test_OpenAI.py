import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_AI")

from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness, SemanticSimilarity
from ragas import evaluate

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from datasets import load_dataset
from ragas import EvaluationDataset

import pandas as pd
import ast

# dataset = load_dataset("explodinggradients/amnesty_qa","english_v3")
# eval_dataset = EvaluationDataset.from_hf_dataset(dataset["eval"])

df = pd.read_excel("/home/halil/Desktop/MeETU/RAG_Model/ragasio/test_dataset_with_response_formatted.xlsx")
df = df[['user_input', 'reference', 'response', 'retrieved_contexts']]
df['retrieved_contexts'] = df['retrieved_contexts'].apply(ast.literal_eval)
eval_dataset = EvaluationDataset.from_pandas(df)

evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
evaluator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

metrics = [
        ## RAG Triad ##
    ## Context Relevance
    LLMContextRecall(llm=evaluator_llm), 

    ## Faithfulness
    FactualCorrectness(llm=evaluator_llm), 
    Faithfulness(llm=evaluator_llm),

    ## Answer Relevance
    SemanticSimilarity(embeddings=evaluator_embeddings)
]

    # 1. Answer Relevance
    #     Metric: SemanticSimilarity
    #         This metric evaluates how semantically similar the generated answer is to the ground truth answer. 
    #         It ensures that the generated response is relevant to the user's query and aligns well with the expected answer.

    # 2. Context Relevance
    #     Metric: LLMContextRecall
    #         This measures the relevance of the retrieved context used to generate the answer. 
    #         It checks whether the retrieved documents or context actually support the generated answer.

    # 3. Faithfulness
    #     Metrics: FactualCorrectness and Faithfulness
    #         FactualCorrectness: Validates if the generated answer is factually correct based on the provided context, ensuring that no hallucinations occur.
    #         Faithfulness: Ensures that the answer is faithful to the retrieved context and does not introduce information not present or supported by the context.


results = evaluate(dataset=eval_dataset, metrics=metrics)

df = results.to_pandas()
df.head()
df.to_excel("ragas_eval_results.xlsx")