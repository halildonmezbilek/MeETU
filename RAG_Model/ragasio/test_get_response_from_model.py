import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import warnings
import pandas as pd
import asyncio
from rag_model import agenerate_chain_output
warnings.filterwarnings("ignore")

file_path = "/home/halil/Desktop/MeETU/Data/TestDataset/FinalTestDataset.xlsx"
df = pd.read_excel(file_path)
questions = df['user_input'].tolist()

async def generate_all_responses(questions):
    results = await asyncio.gather(*(agenerate_chain_output(question) for question in questions))
    
    responses = [result.get("response") for result in results]
    retrieved_contexts = [[context.page_content for context in result.get("contexts")] for result in results]
    
    return responses, retrieved_contexts

async def main():
    responses, retrieved_contexts = await generate_all_responses(questions)
    df['response'] = responses
    df['retrieved_contexts'] = retrieved_contexts
    
    output_file = "test_dataset_with_response.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Responses and contexts saved to {output_file}")

asyncio.run(main())