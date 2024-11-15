import pandas as pd
import re
import ast
df = pd.read_excel("test_dataset_with_response.xlsx")
def reference_contexts_formatter(row):
    _t = row.replace("\\n", "\n")
    _t = re.split(r'\n{2}Entry \d+\n{2}', _t)[1:]
    return _t
df.reference_contexts = df.reference_contexts.apply(reference_contexts_formatter)

def retrieved_contexts_formatter(row):
    _t = ast.literal_eval(row)
    return _t
df.retrieved_contexts = df.retrieved_contexts.apply(retrieved_contexts_formatter)


df.to_excel("test_dataset_with_response_formatted.xlsx")