import asyncio
import streamlit as st
import json
import os
import time
from rag_model import MeETUAssistant
from uuid import uuid4
import base64


# UI PARTS 
st.set_page_config(page_title="MeETU", page_icon="logo.png")


# Function to encode the MeETU logo in Base64 
def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Encode the MeETU logo
encoded_image = get_base64_image("MEETU_BOT_transparant.png")

# UI parts
st.markdown(
    f"""
    <style>
    .custom-logo {{
        position: absolute;
        top: 100px;  
        left: -350px; 
        width: 300px; 
    }}
    .about-meetu{{
        position: relative;
        top: 1px; 
        right: -775px; 
        text-align: left;
        width: 300px; 
    }}

    .disclaimer{{
        position: relative;
        top: 20px; 
        right: -775px;
        color: gray;
        font-size: small;
        width: 300px;
    }}

    </style>
    <img src="data:image/png;base64,{encoded_image}" class="custom-logo">

    <div class="about-meetu">
        <h2>Hi, I am MeETU</h2>
        <p>which is a chatbot designed to assist users with questions about METU (Middle East Technical University).</p>
        <h3>My features:</h3>
        <ul>
            <li>Provides information about programs, campus life, and facilities.</li>
            <li>Answers application-related queries.</li>
            <li>Offers guidance on university processes.</li>
        </ul>
        <p>Whether you're a prospective student or a curious visitor, as MeETU I am here to help you!</p>
    </div>
    
    <div class="disclaimer">
    <em>MeETU may make errors since an AI algorithm drives all outputs.</em>
    </div>
    """
    ,
    unsafe_allow_html=True,
)



USER_HISTORY_DIR = 'user_history'
os.makedirs(USER_HISTORY_DIR, exist_ok=True)


if "session_id" not in st.session_state:
    session_id_param = st.query_params.get("session_id", [str(uuid4())])
    st.session_state.session_id = ''.join(session_id_param)

session_id = st.session_state.session_id

DB_FILE = os.path.join(USER_HISTORY_DIR, f'{session_id}.json')

def main():
    meetu_assistant = MeETUAssistant(
            isstreamlitapp=False,
            embedding_model_name="all-MiniLM-L6-v2",
            vectorstore_dir="path/to/vectorstore",
            llm_repo_id="your_repo_id",
            llm_api_token="your_api_token",
            max_new_tokens=3500,
            search_type="mmr",
            top_k=5,
            temperature=0.3
        )
    

    st.title("Meet METU with MeETU")  

    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, 'r') as file:
                db = json.load(file)
            st.session_state.messages = db.get('chat_history', [])
        except json.JSONDecodeError:
            db = {'chat_history': []}
            st.session_state.messages = []
            update_db(st.session_state.messages)
    else:
        db = {'chat_history': []}
        st.session_state.messages = []
        update_db(st.session_state.messages)

    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message["role"] == "assistant" and "feedback" not in message:
                feedback = st.feedback("thumbs", key=f"feedback_{i}")
                if feedback is not None:
                    st.session_state.messages[i]["feedback"] = "positive" if feedback == 1 else "negative"
                    update_db(st.session_state.messages)
            elif "feedback" in message:
                feedback_text = (
                    "Thank you for your positive feedback!" if message["feedback"] == "positive" 
                    else "Thank you for the feedback, we’ll work on improving!"
                )
                st.write(feedback_text)

    if prompt := st.chat_input("Ask me anything about METU!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        start_time = time.time()
        #response_content = generate_response(prompt)
        response_content = asyncio.run(meetu_assistant.agenerate_response(prompt))
        response_time = time.time() - start_time

        with st.chat_message("assistant"):
            st.markdown(response_content)
        
        st.session_state.messages.append({"role": "assistant", "content": response_content})

        update_db(st.session_state.messages)

        st.write(f"_Response generated in {round(response_time, 3)} seconds_")
        st.rerun()



def update_db(messages):
    db = {'chat_history': messages}
    with open(DB_FILE, 'w') as file:
        json.dump(db, file, indent=2)

if __name__ == '__main__':
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    main()
