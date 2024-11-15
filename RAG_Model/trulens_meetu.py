from trulens.core import Feedback, TruSession
from trulens.providers.litellm import LiteLLM
from trulens.apps.langchain import TruChain
from trulens.dashboard import run_dashboard

from rag_model import rag_chain
from trulens.apps.custom import TruCustomApp
import numpy as np
from trulens.core import Select
import pandas as pd
import json
from tqdm import tqdm
import os
from dotenv import load_dotenv
load_dotenv()

ollama_model_name = "hf.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:Q6_K"
provider = LiteLLM(
    model_engine=f"ollama/{ollama_model_name}", 
    api_base="http://localhost:11434",
)

session = TruSession()
session.reset_database()

try:
    f_answer_relevance = Feedback(
        provider.relevance_with_cot_reasons, name="Answer Relevance"
    ).on_input_output()

    context = TruChain.select_context(rag_chain)

    f_groundedness = (
        Feedback(
            provider.groundedness_measure_with_cot_reasons, name="Groundedness"
        )
        .on(context.collect())  # collect context chunks into a list
        .on_output()
    )

    f_context_relevance = (
        Feedback(
            provider.context_relevance_with_cot_reasons, name="Context Relevance"
        )
        .on_input()
        .on(context)
        .aggregate(np.mean)
    )

    tru_recorder = TruChain(
        rag_chain,
        app_name="ChatApplication",
        app_version="Chain1",
        feedbacks=[f_answer_relevance, f_context_relevance, f_groundedness],
    )

    with tru_recorder as recording:
        llm_response = rag_chain.invoke("How can I connect wifi?")

    records, feedback = session.get_records_and_feedback()

    records.to_json("records.json", indent=2)

    print(session.get_leaderboard())

except Exception as e:
    print("Error setting up feedback functions or retrieving results:", e)

run_dashboard(session)
