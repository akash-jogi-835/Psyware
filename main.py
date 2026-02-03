import streamlit as st
import datetime
import uuid
import requests

# Use your Production URL and ensure the n8n workflow is toggled to 'Active'
N8N_WEBHOOK_URL = "https://akashaigents.app.n8n.cloud/webhook/digital-wellbeing" 

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def create_new_session():
    session_id = str(uuid.uuid4())
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    st.session_state.sessions[session_id] = {
        "session_id": session_id,
        "date": date,
        "messages": [],
        "stress_level": None
    }
    st.session_state.current_session_id = session_id

# Initialize session state
if 'sessions' not in st.session_state:
    st.session_state.sessions = {}

if 'current_session_id' not in st.session_state:
    create_new_session()

# Sidebar
st.sidebar.title("StressSense")
st.sidebar.header("Recent Chats")

# List recent chats
sessions = dict(
    sorted(
        st.session_state.sessions.items(),
        key=lambda x: x[1]["date"],
        reverse=True
    )
)
for sid, sess in sessions.items():
    last_msg = sess["messages"][-1]["text"] if sess["messages"] else "No messages"
    preview = last_msg[:40] + "..." if len(last_msg) > 40 else last_msg
    stress = sess["stress_level"] or "Not assessed"
    if st.sidebar.button(
        label=f"{sess['date']} - {preview} ({stress})",
        key=f"session_{sid}"
    ):
        st.session_state.current_session_id = sid
        st.rerun()

# New Check-in button
if st.sidebar.button("➕ New Check-in"):
    create_new_session()
    st.rerun()

# Main panel
current = st.session_state.sessions[st.session_state.current_session_id]

# Display messages
for msg in current["messages"]:
    with st.chat_message(msg["sender"]):
        st.write(msg["text"])
        st.caption(msg["timestamp"][11:])  # HH:MM

# Chat input
prompt = st.chat_input("Type your message...")
if prompt:
    # Add user message to state
    current["messages"].append({"sender": "user", "text": prompt, "timestamp": now()})
    
    # Display the user message immediately for responsiveness
    st.rerun()

# Logic to handle n8n communication
if current["messages"] and current["messages"][-1]["sender"] == "user":
    with st.spinner("StressSense is thinking..."):
        try:
            # 1. Prepare payload compatible with your n8n JavaScript 'reach-back' code
            payload = {
                "session_id": st.session_state.current_session_id,
                "body": {
                    "messages": [{"text": current["messages"][-1]["text"]}]
                }
            }
            
            # 2. POST request to n8n
            response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=30)
            
            # 3. Enhanced error checking for the 'line 1 column 1' error
            if response.status_code == 200:
                try:
                    data = response.json()
                    # Targeting the 'message' key returned by your JavaScript node
                    assistant_text = data.get("message", "No message found.")
                    
                    # Update the sidebar's stress level dynamically
                    current["stress_level"] = data.get("stress_level", "Not assessed")
                except ValueError:
                    assistant_text = "The brain sent back a non-JSON response. Check n8n production settings."
            else:
                assistant_text = f"Connection error: {response.status_code}"
                
        except requests.exceptions.RequestException as e:
            assistant_text = f"Network error: Could not reach the n8n agent. {str(e)}"

    # 4. Append assistant response and refresh
    current["messages"].append({
        "sender": "assistant",
        "text": assistant_text,
        "timestamp": now()
    })

    st.rerun()

