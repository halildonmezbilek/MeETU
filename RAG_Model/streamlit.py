import streamlit as st
import os
from dotenv import load_dotenv
from model import initialize_components, generate_response, evaluate_performance

load_dotenv()

retriever, wrapped_llm = initialize_components()

st.set_page_config(page_title="MeETU")
st.title("MeETU Chat Assistant")

user_question = st.text_input("Your Question:")

if st.button("Ask") and user_question:
    st.write("Generating response... please wait.")
    response_content = generate_response(retriever, wrapped_llm, user_question)
    
    st.subheader("Response:")
    st.write(response_content)
    
    st.subheader("Relevant Documents:")
    relevant_docs = retriever.get_relevant_documents(user_question)
    for doc in relevant_docs:
        st.write(f"- {doc['content']}")

else:
    st.write("Please enter a question and click 'Ask' to get started.")
