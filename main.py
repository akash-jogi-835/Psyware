# coding=utf-8
import streamlit as st
import requests
import json
import uuid

# --- STREAMLIT PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Psyaware | Digital Well-being",
    page_icon="",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom, #f0f2f6, #ffffff);
        }
        .main-title {
            font-size: 3rem;
            font-weight: 800;
            color: #1E3A8A;
            text-align: center;
            margin-top: -50px;
        }
        .sub-title {
            font-size: 1.2rem;
            color: #4B5563;
            text-align: center;
            margin-bottom: 2rem;
        }
        .sidebar-header {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- FUNCTION DEFINITION ---
def query_chatbot(session_id, user_message, conversation_history):
    url = "https://superexplicitly-nonderogatory-eleanor.ngrok-free.dev/webhook/stressagent"

    # Format history as clean list for Agent 1 to read
    formatted_history = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in conversation_history
    ]

    payload_dict = {
        "session": session_id,
        "message": user_message,
        "conversation_history": formatted_history
    }
    payload = json.dumps(payload_dict)
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        response_json = response.json()

        if isinstance(response_json, list):
            data = response_json[0]
        else:
            data = response_json
        return list(data.values())[0]
    except Exception as e:
        return f"I'm having a little trouble connecting. (Error: {e})"

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<p class="sidebar-header"> Psyaware Control</p>', unsafe_allow_html=True)
    st.info("Analyzing psychosomatic patterns for a balanced digital life.")

    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.session_id = uuid.uuid4().hex
        st.rerun()

    st.divider()
    st.caption("🔒 Secure Session Active")

# --- UI HEADER ---
st.markdown('<p class="main-title"> Psyaware</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Digital Well-being & Stress Analyzer</p>', unsafe_allow_html=True)

# --- SESSION STATE MANAGEMENT ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = uuid.uuid4().hex

# --- CHAT HISTORY VISUALIZATION ---
for message in st.session_state.messages:
    avatar_choice = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar_choice):
        st.markdown(message["content"])

# --- USER INPUT ---
if prompt := st.chat_input("How are you feeling today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Call the n8n webhook — passing full history BEFORE appending current message
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Analyzing patterns..."):
            ai_response = query_chatbot(
                session_id=st.session_state.session_id,
                user_message=prompt,
                conversation_history=st.session_state.messages  # full history including current
            )
            st.markdown(ai_response)

    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
