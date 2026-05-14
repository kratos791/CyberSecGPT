import streamlit as st
from groq import Groq
from pypdf import PdfReader
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PDF Analyzer",
    layout="wide"
)

# ---------------- GROQ ----------------
client = Groq(
    api_key= os.getenv("GROQ_API_KEY")
)

# ---------------- EMBEDDINGS ----------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f3f4f6;
}

.upload-box {
    background: white;
    padding: 30px;
    border-radius: 24px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.05);
}

.answer-box {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
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
📄 PDF Intelligence Analyzer
</div>

<div class="subtitle">
Upload cybersecurity PDFs and ask questions using AI + RAG.
</div>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

# ---------------- PROCESS PDF ----------------
if uploaded_file:

    with st.spinner("Reading PDF..."):

        pdf_reader = PdfReader(uploaded_file)

        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text()

        # Split text
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_text(text)

        # Create vector DB
        vectorstore = FAISS.from_texts(
            chunks,
            embedding_model
        )

    st.success("PDF processed successfully.")

    # ---------------- QUESTION INPUT ----------------
    question = st.text_input(
        "Ask question from PDF"
    )

    # ---------------- ASK ----------------
    if st.button("Analyze PDF"):

        with st.spinner("Analyzing..."):

            # Similar chunks
            docs = vectorstore.similarity_search(
                question,
                k=3
            )

            context = "\n".join(
                [doc.page_content for doc in docs]
            )

            # GROQ RESPONSE
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                        You are a cybersecurity PDF assistant.

                        Answer ONLY using the provided PDF context.

                        Context:
                        {context}
                        """
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = completion.choices[0].message.content

        st.markdown(f"""
        <div class="answer-box">

        <h3>AI Response</h3>

        <p>{answer}</p>

        </div>
        """, unsafe_allow_html=True)