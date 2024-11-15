from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.testset import TestsetGenerator
from ragas import RunConfig
import random

path = "markdownschunked"
loader = DirectoryLoader(path, glob="**/*.md")
docs = loader.load()
seed = 985
random.seed(seed)
docs = random.sample(docs, 9)

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_AI")

generator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini", temperature=0.2))
generator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

config = RunConfig(
    log_tenacity=True,
    max_workers=4,
    max_retries=3,
    seed=seed

)

generator = TestsetGenerator(llm=generator_llm, embedding_model=generator_embeddings)
dataset = generator.generate_with_langchain_docs(docs, testset_size=100, run_config=config, with_debugging_logs=True)
df = dataset.to_pandas()
print(df)
df.to_excel("MeETUTestDataset.xlsx")