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
        top: 10px; 
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
    .about_us{{
        position: relative;
        top: 20px;
        left: -350px;
        width: 275px;
        font-size: small;
        color: gray;
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
    
    <div class="about_us">
        <em>MeETU is designed by Ladies and Gentleman team.</em>
        <em>Team members: Halil İbrahim Dönmezbilek, Merve Ekiz, Nilsu Şahin, Faize Yıldız</em>
    </div>
    """
    ,
    unsafe_allow_html=True,
)


# Directory to store user chat history
USER_HISTORY_DIR = 'user_history'
os.makedirs(USER_HISTORY_DIR, exist_ok=True)

# Initialize a session ID if not already present in session state
if "session_id" not in st.session_state:
    session_id_param = st.query_params.get("session_id", [str(uuid4())])
    st.session_state.session_id = ''.join(session_id_param)

session_id = st.session_state.session_id

# Path to the database file for storing chat history
DB_FILE = os.path.join(USER_HISTORY_DIR, f'{session_id}.json')

# HALLUCINATIONS HANDLING FOR SOME QUERIES

# since the model sees hallucinations sometimes
# add a default response to greetings queries
def is_greeting(query):
    greetings = ["hi","hello","hey","hi meetu","hello meetu", "hey meetu"]
    return query.strip().lower() in greetings

# since the model sees hallucinations sometimes
# add a default response to appreciations queries
def is_appreciation(query):
    appreciations = ["thank you", "thanks", "well done", "great job", "good bot", "thanks a lot", "thanks lot"
                     "thank you meetu", "thanks meetu", "well done meetu", "great job meetu", "good bot meetu", "thanks lot meetu"]
    return query.strip().lower() in appreciations

# since the model sees hallucinations sometimes
# add a default response to TURKISH greetings queries
def is_selemlama(query):
    selamlamalar = ["selam","merhaba","selam meetu","merhaba meetu"]
    return query.strip().lower() in selamlamalar

# since the model sees hallucinations sometimes
# add a default response to TURKISH appreciations queries
def is_tesekkur(query):
    tesekkurler = ["teşekkürler","teşekkür ederim", "çok teşekkürler", "çok teşekkür ederim", "sağ ol", "çok sağ ol", "çok yardımcı oldun",
                    "teşekkürler meetu","teşekkür ederim meetu", "çok teşekkürler meetu", "çok teşekkür ederim meetu", 
                    "sağ ol meetu", "çok sağ ol meetu", "çok yardımcı oldun meetu"]
    return query.strip().lower() in tesekkurler


def main():
    """
    Main function to manage the chat interface, handle user input, 
    display chat history, and generate responses.
    """
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
            # Load existing chat history from the database
            with open(DB_FILE, 'r') as file:
                db = json.load(file)
            st.session_state.messages = db.get('chat_history', [])
        except json.JSONDecodeError:
            # Handle corrupted or empty JSON files
            db = {'chat_history': []}
            st.session_state.messages = []
            update_db(st.session_state.messages)
    else:
        # Initialize a new chat history if no database file exists
        db = {'chat_history': []}
        st.session_state.messages = []
        update_db(st.session_state.messages)

    # Display each message in the chat history
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Collect feedback for assistant responses
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

    # Process new user input from the chat interface
    if prompt := st.chat_input("Ask me anything about METU!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # greeting queries check
        if is_greeting(prompt):
            response_content = "Hello! You've reached METU's AI assistant. I'm here to help you with any questions you might have about METU."
            start_time = time.time()
            response_time = time.time() - start_time
        
        # TURKISH greeting queries check
        elif is_selemlama(prompt):
            response_content = "Merhaba! ODTÜ'nün AI asistanına ulaştınız. ODTÜ ile ilgili herhangi bir sorunuzda size yardımcı olmak için buradayım."
            start_time = time.time()
            response_time = time.time() - start_time
        
        # appreciation queries check
        elif is_appreciation(prompt):
            response_content = "You're welcome! I'm glad I could help. 😊"
            start_time = time.time()
            response_time = time.time() - start_time
        
        # TURKISH appreciation queries check
        elif is_tesekkur(prompt):
            response_content = "Rica ederim! Yardımcı olabildiğime sevindim. 😊"
            start_time = time.time()
            response_time = time.time() - start_time       
        
        # GENERAL QUERY part
        else:
            with st.chat_message("user"):
                st.markdown(prompt)
            start_time = time.time()

            # Generate response asynchronously using agenerate_response from meetu_assistant class in rag_model.py file
            response_content = asyncio.run(meetu_assistant.agenerate_response(prompt))
            response_time = time.time() - start_time
            
            with st.chat_message("assistant"):
                st.markdown(response_content)

        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_content})
        
        update_db(st.session_state.messages)
       
        st.write(f"_Response generated in {round(response_time, 3)} seconds_")
        st.rerun()



def update_db(messages):
    """
    Update the database file with the current chat history.
    """
    db = {'chat_history': messages}
    with open(DB_FILE, 'w') as file:
        json.dump(db, file, indent=2)

if __name__ == '__main__':
    # Ensure the messages list is initialized in session state
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    
    main()