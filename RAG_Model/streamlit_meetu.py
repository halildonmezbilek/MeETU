import streamlit as st
st.set_page_config(page_title="MeETU", page_icon="logo.png")


import json
import os
import time
from rag_model import generate_response
from uuid import uuid4


USER_HISTORY_DIR = 'user_history'
os.makedirs(USER_HISTORY_DIR, exist_ok=True)


if "session_id" not in st.session_state:
    session_id_param = st.query_params.get("session_id", [str(uuid4())])
    st.session_state.session_id = ''.join(session_id_param)

session_id = st.session_state.session_id

DB_FILE = os.path.join(USER_HISTORY_DIR, f'{session_id}.json')

def main():
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
        response_content = generate_response(prompt)
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
