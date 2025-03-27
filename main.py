# main.py (FastAPI entry point)
from fastapi import FastAPI # type: ignore
from routes import chat, websocket
from database import connect_db
import uvicorn # type: ignore

app = FastAPI()

# Connect to the 
connect_db()

# Include routers
app.include_router(chat.router)
app.include_router(websocket.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)