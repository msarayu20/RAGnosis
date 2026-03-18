import streamlit as st
from app import ask

# Page config
st.set_page_config(
    page_title="ContextForge",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS (this is the secret 🔥)
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.chat-container {
    max-width: 700px;
    margin: auto;
}

.user-msg {
    background-color: #1f2937;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 10px;
    text-align: right;
    color: white;
}

.bot-msg {
    background-color: #111827;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 20px;
    text-align: left;
    color: #e5e7eb;
}

.title {
    text-align: center;
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 20px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🧠 ContextForge</div>', unsafe_allow_html=True)

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input
query = st.chat_input("Ask something...")

if query:
    # Save user message
    st.session_state.messages.append(("user", query))

    # Get response
    response = ask(query)

    # Save bot response
    st.session_state.messages.append(("bot", response))

# Display chat
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)