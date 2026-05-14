import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Chatbot",
    layout="wide"
)

# ---------------- GROQ CLIENT ----------------
client = Groq(
    api_key= os.getenv("GROQ_API_KEY"))

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f3f4f6;
}

.chat-container {
    background: white;
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.user-msg {
    background: #111827;
    color: white;
    padding: 15px;
    border-radius: 16px;
    margin-top: 10px;
}

.bot-msg {
    background: #f9fafb;
    color: #111827;
    padding: 15px;
    border-radius: 16px;
    margin-top: 10px;
    border: 1px solid #e5e7eb;
}

.title {
    font-size: 42px;
    font-weight: 800;
    color: #111827;
}

.subtitle {
    color: #6b7280;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("""
<div class="title">
🤖 AI Cybersecurity Chatbot
</div>

<div class="subtitle">
Ask cybersecurity questions using Groq-powered AI.
</div>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SHOW CHAT HISTORY ----------------
for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(f"""
        <div class="user-msg">
        <b>You:</b><br><br>
        {message["content"]}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="bot-msg">
        <b>CyberSecGPT:</b><br><br>
        {message["content"]}
        </div>
        """, unsafe_allow_html=True)

# ---------------- INPUT ----------------
prompt = st.chat_input("Ask a cybersecurity question...")

# ---------------- GENERATE RESPONSE ----------------
if prompt:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Show user message
    st.markdown(f"""
    <div class="user-msg">
    <b>You:</b><br><br>
    {prompt}
    </div>
    """, unsafe_allow_html=True)

    # AI RESPONSE
    with st.spinner("CyberSecGPT is thinking..."):

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an advanced AI cybersecurity assistant.
                    Help users with:
                    - Cybersecurity concepts
                    - Threat intelligence
                    - Malware analysis
                    - Ethical hacking
                    - SOC operations
                    - SIEM
                    - Incident response
                    - AI security
                    - Governance
                    """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response = completion.choices[0].message.content

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Show AI response
    st.markdown(f"""
    <div class="bot-msg">
    <b>CyberSecGPT:</b><br><br>
    {response}
    </div>
    """, unsafe_allow_html=True)
