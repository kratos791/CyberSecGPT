import streamlit as st

st.set_page_config(
    page_title="CyberSecGPT",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #f4f7fb;
}

.block-container {
    padding-top: 2rem;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 20px;
    color: #6b7280;
    margin-bottom: 40px;
}

.card {
    padding: 28px;
    border-radius: 24px;
    color: #111827;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    transition: 0.3s;
    height: 220px;
}

.card:hover {
    transform: translateY(-5px);
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 15px;
}

.card-desc {
    color: #6b7280;
    margin-top: 12px;
    font-size: 15px;
    line-height: 1.6;
}

.blue {
    background: linear-gradient(135deg,#dbeafe,#eff6ff);
}

.red {
    background: linear-gradient(135deg,#fee2e2,#fff1f2);
}

.green {
    background: linear-gradient(135deg,#dcfce7,#f0fdf4);
}

.purple {
    background: linear-gradient(135deg,#ede9fe,#f5f3ff);
}

.orange {
    background: linear-gradient(135deg,#ffedd5,#fff7ed);
}

.stats-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 10px rgba(0,0,0,0.04);
}

.stats-number {
    font-size: 34px;
    font-weight: 800;
}

.stats-label {
    color: gray;
}

/* HIDE STREAMLIT DEFAULT SIDEBAR NAVIGATION */
section[data-testid="stSidebarNav"] {
    display: none;
}

/* CUSTOM SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e7eb;
}

.sidebar-title {
    font-size: 28px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 8px;
}

.sidebar-subtitle {
    color: gray;
    margin-bottom: 30px;
}

.sidebar-section {
    font-size: 13px;
    color: gray;
    margin-top: 25px;
    margin-bottom: 10px;
    font-weight: 600;
    text-transform: uppercase;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HIDE DEFAULT STREAMLIT SIDEBAR NAV
# ==========================================

st.markdown("""
<style>

/* Hide default multipage navigation */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5e7eb;
}

/* Remove top Streamlit decoration */
header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# CUSTOM SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# 🛡️ CyberSecGPT")
    st.caption("AI Powered Cybersecurity Platform")

    st.divider()

    st.markdown("### Navigation")

    st.page_link("app.py", label="🏠 Dashboard")

    st.page_link(
        "pages/1_🤖_AI_Chatbot.py",
        label="🤖 AI Chatbot"
    )

    st.page_link(
        "pages/2_📄_PDF_Analyzer.py",
        label="📄 PDF Analyzer"
    )

    st.page_link(
        "pages/3_🛡️_Threat_Intelligence.py",
        label="🛡️ Threat Intelligence"
    )

    st.page_link(
        "pages/4_⚖️_AI_Governance.py",
        label="⚖️ AI Governance"
    )

    st.page_link(
        "pages/5_🎯_Interview_Preparation.py",
        label="🎯 Interview Prep"
    )
    st.divider()

    st.success("🟢 System Active")
# ==========================================
# HERO SECTION
# ==========================================

st.markdown(
    '<div class="hero-title">🛡️ CyberSecGPT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">AI Powered Cybersecurity Intelligence & Analysis Platform</div>',
    unsafe_allow_html=True
)

# ==========================================
# STATS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">24/7</div>
        <div class="stats-label">Monitoring</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">AI</div>
        <div class="stats-label">Threat Detection</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">Live</div>
        <div class="stats-label">Threat Feed</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">PDF</div>
        <div class="stats-label">Analysis Engine</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# FEATURE CARDS
# ==========================================

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card blue">
        <div style="font-size:50px;">🤖</div>
        <div class="card-title">AI Cybersecurity Chatbot</div>
        <div class="card-desc">
            Ask cybersecurity questions, analyze threats, learn concepts,
            and get AI-powered security guidance instantly.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card red">
        <div style="font-size:50px;">📄</div>
        <div class="card-title">PDF Security Analyzer</div>
        <div class="card-desc">
            Upload cybersecurity reports, research papers,
            and documents for intelligent AI analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card green">
        <div style="font-size:50px;">🛡️</div>
        <div class="card-title">Threat Intelligence</div>
        <div class="card-desc">
            Monitor live CVEs, analyze malicious IPs,
            and access real-time cybersecurity intelligence feeds.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card purple">
        <div style="font-size:50px;">🎯</div>
        <div class="card-title">Interview Preparation</div>
        <div class="card-desc">
            Practice cybersecurity interview questions,
            HR rounds, technical assessments, and AI mock interviews.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    <div class="card orange">
        <div style="font-size:50px;">🏢</div>
        <div class="card-title">AI Governance</div>
        <div class="card-desc">
            Learn AI regulations, governance frameworks,
            responsible AI, and compliance standards.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card blue">
        <div style="font-size:50px;">🌐</div>
        <div class="card-title">Industry Insights</div>
        <div class="card-desc">
            Explore cybersecurity trends, latest technologies,
            attack techniques, and industry developments.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<center>
    <p style="color:gray;">
        Built with ❤️ using Streamlit, Groq AI, LangChain & Cyber Threat Intelligence APIs
    </p>
</center>
""", unsafe_allow_html=True)