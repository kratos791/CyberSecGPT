import streamlit as st

st.set_page_config(
    page_title="AI Governance",
    layout="wide"
)

st.title("⚖️ AI Governance Center")
st.caption("Ethical AI & Cybersecurity Governance")

# ====================================
# OVERVIEW
# ====================================

st.markdown("""
Artificial Intelligence Governance ensures that AI systems are:

- Ethical
- Transparent
- Secure
- Fair
- Explainable
- Privacy focused
""")

st.write("")

# ====================================
# PRINCIPLES
# ====================================

principles = [
    ("🔒 Security", "Protect AI systems from attacks and misuse."),
    ("⚖️ Fairness", "Avoid bias and discrimination in AI decisions."),
    ("👁️ Transparency", "Explain how AI systems make decisions."),
    ("🛡️ Privacy", "Protect user and organizational data."),
    ("📜 Compliance", "Follow regulations and cybersecurity standards."),
    ("🤝 Accountability", "Organizations remain responsible for AI decisions."),
]

col1, col2 = st.columns(2)

for i, item in enumerate(principles):

    title, desc = item

    card = f"""
    <div style="
        background:white;
        padding:22px;
        border-radius:18px;
        margin-bottom:18px;
        box-shadow:0 4px 12px rgba(0,0,0,0.05);
        border:1px solid #e5e7eb;
    ">
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
    """

    if i % 2 == 0:
        col1.markdown(card, unsafe_allow_html=True)
    else:
        col2.markdown(card, unsafe_allow_html=True)

# ====================================
# AI RISKS
# ====================================

st.subheader("🚨 AI Security Risks")

risks = [
    "Prompt Injection",
    "Model Poisoning",
    "Data Leakage",
    "Deepfake Abuse",
    "AI Hallucinations",
    "Automated Cyber Attacks",
]

for risk in risks:
    st.warning(risk)

# ====================================
# FRAMEWORKS
# ====================================

st.subheader("📚 Governance Frameworks")

frameworks = [
    "NIST AI RMF",
    "ISO/IEC 42001",
    "GDPR",
    "OWASP Top 10 for LLMs",
    "EU AI Act",
]

for fw in frameworks:
    st.success(fw)