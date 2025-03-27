from fastapi import WebSocket, APIRouter
from database import db
from routes.chat import generate_summary

router = APIRouter()

@router.websocket("/ws/summarize/{conversation_id}")
async def websocket_endpoint(websocket: WebSocket, conversation_id: str):
    await websocket.accept()
    chats = await db.chats.find({"conversation_id": conversation_id}).to_list(100)
    messages = "\n".join([chat["message"] for chat in chats])
    summary = await generate_summary(messages)
    await websocket.send_text(summary)
    await websocket.close()