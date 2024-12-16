import asyncio
import streamlit as st

# Set the page configuration with a title and an icon
st.set_page_config(page_title="MeETU", page_icon="logo.png")

import json
import os
import time
from rag_model import generate_response, agenerate_response
from uuid import uuid4

# Directory to store user chat history
USER_HISTORY_DIR = 'user_history'
os.makedirs(USER_HISTORY_DIR, exist_ok=True)  # Ensure the directory exists

# Initialize a session ID if not already present in session state
if "session_id" not in st.session_state:
    # Check for a session ID in query parameters or generate a new one
    session_id_param = st.query_params.get("session_id", [str(uuid4())])
    st.session_state.session_id = ''.join(session_id_param)

session_id = st.session_state.session_id  # Retrieve the current session ID

# Path to the database file for storing chat history
DB_FILE = os.path.join(USER_HISTORY_DIR, f'{session_id}.json')

def main():
    """
    Main function to manage the chat interface, handle user input, 
    display chat history, and generate responses.
    """
    if os.path.exists(DB_FILE):  # Check if the database file exists
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
        with st.chat_message(message["role"]):  # Show messages based on role (user/assistant)
            st.markdown(message["content"])

            # Collect feedback for assistant responses
            if message["role"] == "assistant" and "feedback" not in message:
                feedback = st.feedback("thumbs", key=f"feedback_{i}")
                if feedback is not None:
                    st.session_state.messages[i]["feedback"] = "positive" if feedback == 1 else "negative"
                    update_db(st.session_state.messages)
            elif "feedback" in message:
                # Display feedback acknowledgment
                feedback_text = (
                    "Thank you for your positive feedback!" if message["feedback"] == "positive" 
                    else "Thank you for the feedback, we’ll work on improving!"
                )
                st.write(feedback_text)

    # Process new user input from the chat interface
    if prompt := st.chat_input("Ask me anything about METU!"):
        # Add user input to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user input
        with st.chat_message("user"):
            st.markdown(prompt)
        
        start_time = time.time()  # Record the start time for response generation

        # Generate response asynchronously using agenerate_response
        response_content = asyncio.run(agenerate_response(prompt))
        response_time = time.time() - start_time  # Calculate response time

        # Display the assistant's response
        with st.chat_message("assistant"):
            st.markdown(response_content)
        
        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_content})

        # Save updated chat history to the database
        update_db(st.session_state.messages)

        # Display response time
        st.write(f"_Response generated in {round(response_time, 3)} seconds_")
        
        # Rerun the script to refresh the interface
        st.rerun()

def update_db(messages):
    """
    Update the database file with the current chat history.
    """
    db = {'chat_history': messages}
    with open(DB_FILE, 'w') as file:
        json.dump(db, file, indent=2)  # Save data in JSON format with indentation for readability

if __name__ == '__main__':
    # Ensure the messages list is initialized in session state
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    main()  # Run the main function
