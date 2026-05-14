import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Interview Preparation",
    layout="wide"
)

# ==========================================
# GROQ CLIENT
# ==========================================

client = Groq(
    api_key= os.getenv("GROQ_API_KEY")
)

# ==========================================
# TITLE
# ==========================================

st.title("🎯 AI Cybersecurity Interview Prep")
st.caption("AI Generated Cybersecurity Interview Questions & Answers")

# ==========================================
# USER INPUT
# ==========================================

role = st.text_input(
    "Enter Job Role or Topic",
    placeholder="SOC Analyst, Penetration Tester, Networking..."
)

difficulty = st.selectbox(
    "Difficulty Level",
    ["Beginner", "Intermediate", "Advanced"]
)

num_questions = st.slider(
    "Number of Questions",
    1,
    10,
    5
)

# ==========================================
# GENERATE BUTTON
# ==========================================

if st.button("🚀 Generate Interview Questions"):

    if role.strip() == "":
        st.warning("Please enter a role or topic.")
        st.stop()

    prompt = f"""
Generate {num_questions} cybersecurity interview questions and answers.

Role/Topic:
{role}

Difficulty:
{difficulty}

Requirements:
- Include practical cybersecurity concepts
- Questions should be technical
- Answers should be detailed but easy to understand
- Format properly using numbering
"""

    with st.spinner("Generating AI Interview Questions..."):

        try:

            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert cybersecurity interviewer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )

            response = completion.choices[0].message.content

            st.success("Interview Questions Generated Successfully")

            st.markdown(f"""
            <div style="
                background:white;
                padding:30px;
                border-radius:20px;
                box-shadow:0 4px 12px rgba(0,0,0,0.05);
                border:1px solid #e5e7eb;
            ">
            {response.replace('\n', '<br>')}
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {str(e)}")

# ==========================================
# QUICK TOPICS
# ==========================================

st.write("")
st.subheader("🔥 Popular Cybersecurity Topics")

topics = [
    "SOC Analyst",
    "Penetration Testing",
    "Network Security",
    "Digital Forensics",
    "Incident Response",
    "Cloud Security",
    "Ethical Hacking",
    "Malware Analysis",
]

cols = st.columns(4)

for i, topic in enumerate(topics):

    with cols[i % 4]:

        st.markdown(f"""
        <div style="
            background:white;
            padding:18px;
            border-radius:16px;
            text-align:center;
            margin-bottom:15px;
            border:1px solid #e5e7eb;
            box-shadow:0 2px 8px rgba(0,0,0,0.04);
        ">
            <b>{topic}</b>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# INTERVIEW TIPS
# ==========================================

st.subheader("💡 Interview Tips")

tips = [
    "Practice networking fundamentals",
    "Understand Linux commands",
    "Learn SIEM concepts",
    "Understand IDS vs IPS",
    "Practice explaining attacks clearly",
    "Study real-world cyber incidents",
]

for tip in tips:
    st.info(tip)

# ==========================================
# FOOTER
# ==========================================

st.caption("CyberSecGPT • AI Powered Interview Preparation")