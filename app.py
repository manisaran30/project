import streamlit as st # type: ignore
import requests
import os
from dotenv import load_dotenv # type: ignore
import google.generativeai as genai # type: ignore
from database import store_chat, get_chat_summary


# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_with_gemini(conversation_text):
    """Summarize chat using Google Gemini AI."""
    if not conversation_text:
        return "No messages to summarize."
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "Summarize the following chat conversation concisely:"
    response = model.generate_content([prompt, conversation_text])
    
    return response.text if response else "No summary available."

# Streamlit UI
st.set_page_config(page_title="Chat Summarization API", page_icon="💬", layout="wide")
st.title("Chat Summarization API 🚀")
st.write("Store and summarize chat conversations using AI-powered API.")

# Input Fields
user_id = st.text_input("Enter User ID:")
conversation_id = st.text_input("Enter Conversation ID:")
message = st.text_area("Enter Chat Message:")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("📩 Store Chat"):
        if user_id and conversation_id and message:
            store_chat(user_id, conversation_id, message)
            st.success("✅ Chat stored successfully!")
        else:
            st.warning("⚠️ Please fill in all fields.")

with col2:
    if st.button("📜 Summarize Chat"):
        if conversation_id:
            chat_text = get_chat_summary(conversation_id)
            ai_summary = summarize_with_gemini(chat_text)
            st.subheader("📢 AI-Generated Summary")
            st.write(ai_summary)
        else:
            st.warning("⚠️ Please enter a Conversation ID.")
