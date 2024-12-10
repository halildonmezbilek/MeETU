from flask import Flask, redirect, session, url_for
from uuid import uuid4
import os
import subprocess

app = Flask(__name__)
app.secret_key = os.urandom(24)

STREAMLIT_PORT = 8501

@app.route('/')
def index():
    session_id = str(uuid4())
    session['session_id'] = session_id
    
    streamlit_url = f"http://localhost:{STREAMLIT_PORT}?session_id={session_id}"
    #streamlit_url = f"http://meetu.halildonmezbilek.com/streamlit/?session_id={session_id}"
    return redirect(streamlit_url)

def run_streamlit():
    subprocess.Popen(["streamlit", "run", "/home/halil/Desktop/MeETU/RAG_Model/streamlit_meetu.py", "--server.port", str(STREAMLIT_PORT), "--server.headless=true"])

if __name__ == '__main__':
    run_streamlit()
    app.run(port=5000)
