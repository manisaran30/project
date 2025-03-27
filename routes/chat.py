from fastapi import APIRouter, HTTPException # type: ignore
from database import db
from models import ChatMessage
from bson import ObjectId # type: ignore
import google.generativeai as genai # type: ignore
import os

router = APIRouter()

# Load API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise HTTPException(status_code=500, detail="Google API Key is missing.")

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)

@router.post("/chats")
async def store_chat(chat: ChatMessage):
    """Store chat message in database."""
    result = await db.chats.insert_one(chat.dict())
    return {"message": "Chat stored", "id": str(result.inserted_id)}

@router.get("/chats/{conversation_id}")
async def retrieve_chats(conversation_id: str):
    """Retrieve all chat messages for a given conversation ID."""
    chats = await db.chats.find({"conversation_id": conversation_id}).to_list(100)
    return [{"id": str(chat["_id"]), **chat} for chat in chats]

@router.post("/chats/summarize")
async def summarize_chat(conversation_id: str):
    """Summarize chat conversation using Google Gemini AI."""
    chats = await db.chats.find({"conversation_id": conversation_id}).to_list(100)
    if not chats:
        raise HTTPException(status_code=404, detail="No chats found")
    
    messages = "\n".join([chat["message"] for chat in chats])
    summary = await generate_summary(messages)
    return {"summary": summary}

async def generate_summary(messages: str):
    """Generate a summary using Google Gemini AI."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = "Summarize the following chat conversation concisely:"
        response = model.generate_content([prompt, messages])

        return response.text if response and response.text else "No summary available."
    except Exception as e:
        return f"Error in summarization: {str(e)}"

@router.get("/users/{user_id}/chats")
async def get_user_chats(user_id: str, page: int = 1, limit: int = 10):
    """Retrieve paginated chat messages for a specific user."""
    chats = await db.chats.find({"user_id": user_id}).skip((page-1)*limit).limit(limit).to_list(limit)
    return [{"id": str(chat["_id"]), **chat} for chat in chats]

@router.delete("/chats/{conversation_id}")
async def delete_chat(conversation_id: str):
    """Delete all chat messages for a specific conversation ID."""
    result = await db.chats.delete_many({"conversation_id": conversation_id})
    return {"message": f"Deleted {result.deleted_count} messages"}
