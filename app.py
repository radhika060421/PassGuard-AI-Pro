import streamlit as st
import random
import string

from password_checker import check_password
from ai_suggestions import generate_suggestion
from database import create_table, save_result

# ==========================
# DATABASE
# ==========================

create_table()

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="PassGuard AI Pro",
    page_icon="🔐",
    layout="centered"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(
        135deg,
        #f8fafc,
        #e0f2fe,
        #ede9fe
    );
}

/* Title */
.title{
    text-align:center;
    color:#2563eb;
    font-size:55px;
    font-weight:bold;
    margin-bottom:10px;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#334155;
    font-size:20px;
    font-weight:600;
    margin-bottom:25px;
}

/* Dark Text */
html, body, p, h1, h2, h3, h4, h5, h6, label, span{
    color:#0f172a !important;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

[data-testid="stMetricValue"]{
    color:#0f172a !important;
    font-weight:bold;
}

[data-testid="stMetricLabel"]{
    color:#475569 !important;
}

/* Input */
.stTextInput input{
    background:white !important;
    color:#0f172a !important;
    border:2px solid #2563eb !important;
    border-radius:12px !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* Placeholder */
.stTextInput input::placeholder{
    color:#64748b !important;
}

/* Buttons */
.stButton button{
    width:100%;
    height:50px;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        90deg,
        #3b82f6,
        #8b5cf6
    );
    color:white !important;
    font-size:18px;
    font-weight:bold;
}

/* Tips Box */
.stInfo{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown(
    '<div class="title">🔐 PassGuard AI Pro</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Password Security Analyzer & Generator</div>',
    unsafe_allow_html=True
)

# ==========================
# DASHBOARD
# ==========================

# ==========================
# PASSWORD INPUT
# ==========================

password = st.text_input(
    "🔑 Enter Your Password",
    type="password",
    placeholder="Enter a strong password..."
)

# ==========================
# ANALYZE BUTTON
# ==========================

if st.button("🔍 Analyze Password"):

    if password:

        score, strength, feedback = check_password(password)

        save_result(
            password,
            score,
            strength
        )

        st.subheader("📊 Security Score")

        st.metric(
            "Password Score",
            f"{score}/100"
        )

        st.progress(score)

        # Strength

        if strength == "Strong":
            st.success("✅ Strong Password")

        elif strength == "Medium":
            st.warning("⚠ Medium Password")

        else:
            st.error("❌ Weak Password")

        # Crack Time

        st.subheader("⏳ Estimated Crack Time")

        if score <= 30:
            st.error("Few Seconds")

        elif score <= 60:
            st.warning("Few Hours")

        elif score <= 80:
            st.info("Several Days")

        else:
            st.success("Several Years")

        # Feedback

        st.subheader("🔒 Security Feedback")

        if feedback:
            for item in feedback:
                st.warning(item)

        # AI Suggestions

        st.subheader("🤖 AI Suggestions")

        suggestions = generate_suggestion(password)

        if suggestions:
            for suggestion in suggestions:
                st.info(suggestion)

        else:
            st.success(
                "Excellent! Your password follows strong security practices."
            )

    else:
        st.error("Please enter a password.")

# ==========================
# PASSWORD GENERATOR
# ==========================

st.divider()

st.subheader("🎲 Strong Password Generator")

if st.button("Generate Strong Password"):

    chars = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )

    generated = "".join(
        random.choice(chars)
        for _ in range(16)
    )

    st.code(generated)

# ==========================
# SECURITY TIPS
# ==========================

st.divider()

st.info("""
🔒 Security Tips

• Use at least 12 characters

• Include uppercase letters

• Include lowercase letters

• Add numbers and special symbols

• Avoid names and birthdays

• Never reuse passwords

• Use a password manager
""")

# ==========================
# FOOTER
# ==========================

st.markdown("""
<div style="
margin-top:30px;
padding:15px;
text-align:center;
background:rgba(255,255,255,0.7);
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
">

<h3 style="color:#111827;">
🔐 PassGuard AI Pro
</h3>

<p style="color:#374151;">
Cybersecurity + Artificial Intelligence Project
</p>

</div>
""", unsafe_allow_html=True)