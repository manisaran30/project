from pydantic import BaseModel # type: ignore
from datetime import datetime
from typing import List

class ChatMessage(BaseModel):
    user_id: str
    conversation_id: str
    message: str
    timestamp: datetime = datetime.utcnow()