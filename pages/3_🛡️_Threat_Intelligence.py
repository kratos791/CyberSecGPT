import streamlit as st
import requests
from datetime import datetime, timedelta, UTC

today = datetime.now(UTC)
last_week = today - timedelta(days=7)
# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Threat Intelligence",
    page_icon="🛡️",
    layout="wide"
)

ABUSE_API = ("cfbfd266e89ef963b4b58ba04190ecacc2d60d56207426d0ac9595f40af69cd43f07d413b4ed8c20")

# ==========================================
# STYLING
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 2rem;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    margin-bottom: 18px;
    border: 1px solid #e6e6e6;
}

.high {
    color: #ff4b4b;
    font-weight: bold;
}

.medium {
    color: orange;
    font-weight: bold;
}

.low {
    color: green;
    font-weight: bold;
}

.title {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 10px;
}

.subtitle {
    color: gray;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown('<div class="title">🛡️ Threat Intelligence Center</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Real-time Cyber Threat Monitoring & Intelligence</div>',
    unsafe_allow_html=True
)

# ==========================================
# IP REPUTATION CHECKER
# ==========================================

st.subheader("🌐 IP Reputation Checker")

ip = st.text_input("Enter IP Address")

if st.button("Analyze IP"):

    if ip.strip() == "":
        st.warning("Please enter an IP address")

    else:
        url = "https://api.abuseipdb.com/api/v2/check"

        querystring = {
            'ipAddress': ip,
            'maxAgeInDays': '90'
        }

        headers = {
            'Accept': 'application/json',
            'Key': ABUSE_API
        }

        response = requests.get(
            url,
            headers=headers,
            params=querystring
        )

        if response.status_code == 200:

            data = response.json()["data"]

            score = data["abuseConfidenceScore"]

            if score >= 70:
                level = "HIGH RISK"
                css = "high"

            elif score >= 30:
                level = "MEDIUM RISK"
                css = "medium"

            else:
                level = "LOW RISK"
                css = "low"

            st.markdown(f"""
            <div class="card">

            <h3>IP Analysis Result</h3>

            <p><b>IP Address:</b> {data['ipAddress']}</p>

            <p><b>Country:</b> {data.get('countryCode', 'N/A')}</p>

            <p><b>ISP:</b> {data.get('isp', 'N/A')}</p>

            <p><b>Domain:</b> {data.get('domain', 'N/A')}</p>

            <p>
            <b>Threat Level:</b>
            <span class="{css}">
            {level}
            </span>
            </p>

            <p>
            <b>Abuse Confidence Score:</b>
            {score}/100
            </p>

            <p>
            <b>Total Reports:</b>
            {data.get('totalReports', 0)}
            </p>

            </div>
            """, unsafe_allow_html=True)

        else:
            st.error("Failed to fetch IP intelligence")

# ==========================================
# LATEST CVEs
# ==========================================

st.divider()

st.subheader("🚨 Latest Critical CVEs")

# Last 7 days CVEs
today = datetime.utcnow()
last_week = today - timedelta(days=7)

pub_start = last_week.strftime("%Y-%m-%dT00:00:00.000")
pub_end = today.strftime("%Y-%m-%dT23:59:59.999")

url = (
    f"https://services.nvd.nist.gov/rest/json/cves/2.0?"
    f"pubStartDate={pub_start}Z&"
    f"pubEndDate={pub_end}Z&"
    f"resultsPerPage=10"
)

response = requests.get(url)

if response.status_code == 200:

    cves = response.json()["vulnerabilities"]

    for item in cves:

        cve = item["cve"]

        cve_id = cve["id"]

        published = cve["published"][:10]

        description = cve["descriptions"][0]["value"]

        # Severity Handling
        severity = "UNKNOWN"
        score = "N/A"
        css = "low"

        try:
            metrics = cve["metrics"]["cvssMetricV31"][0]

            severity = metrics["cvssData"]["baseSeverity"]

            score = metrics["cvssData"]["baseScore"]

            if severity == "CRITICAL":
                css = "high"

            elif severity == "HIGH":
                css = "high"

            elif severity == "MEDIUM":
                css = "medium"

            else:
                css = "low"

        except:
            pass

        st.markdown(f"""
        <div class="card">

        <h3>{cve_id}</h3>

        <p>
        <span class="{css}">
        {severity}
        </span>

        | CVSS Score: <b>{score}</b>
        </p>

        <p><b>Published:</b> {published}</p>

        <p>{description[:300]}...</p>

        </div>
        """, unsafe_allow_html=True)

else:
    st.error("Failed to fetch CVE data")