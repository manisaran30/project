chat Summarization API 🚀 
A simple API for storing, retrieving, and summarizing chat conversations using FastAPI, MongoDB, and Gemini AI(https://chatsummary.streamlit.app/).  

---

📌 Features  
- ✅ Store Chats: Save user messages to MongoDB.  
- ✅ Retrieve Chats: Fetch chat history based on conversation ID.  
- ✅ Summarization: Generate AI-powered chat summaries using Google Gemini AI.  
- ✅ User Interface: Streamlit-based frontend for interaction.  

---

🛠️ Tech Stack  
- Backend: FastAPI (Python)  
- Database: MongoDB Atlas (Cloud-based)  
- Frontend: Streamlit  
- **AI Model: Google Gemini AI  
- Deployment: (Optional) Render, Railway, AWS, GCP  

---

🚀 Getting Started  

1⃣ Clone the Repository  
```sh
git clone https://github.com/manisaran30/project.git
cd project
```

2⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

3⃣ Set Up MongoDB  
- Create a MongoDB Atlas account.  
- Replace `MONGO_URI` in `database.py` with your MongoDB connection string.  

4⃣ Run FastAPI Backend
```sh
uvicorn main:app --reload
```
- API will be available at: `http://127.0.0.1:8000/docs`

5⃣ Run Streamlit Frontend  
```sh
streamlit run app.py
```
- Open browser at `http://localhost:8501`

---
🖥️ API Endpoints
| Method | Endpoint | Description |  
|--------|---------|-------------|  
| `POST` | `/chats` | Store chat message |  
| `GET` | `/chats/{conversation_id}` | Retrieve chat history |  
| `POST` | `/summarize` | Summarize conversation |  

---
💂‍ Project Structure 
```
📺 project  
 ┣ 📚 app.py             # Streamlit frontend  
 ┣ 📚 main.py            # FastAPI backend  
 ┣ 📚 database.py        # MongoDB database connection  
 ┣ 📚 models.py          # Pydantic models  
 ┣ 📚 routes/chat.py     # Chat-related API routes  
 ┣ 📚 routes/websocket.py# WebSocket (if needed)  
 ┣ 📚 requirements.txt   # Dependencies  
 ┗ 📚 README.md          # Project documentation  
```

---

🚀 Deployment  
Option 1: Deploy FastAPI on Render/Railway  
- Create a **Render** or **Railway** account.  
- Deploy using your `main.py` entry point.  

Option 2: Deploy Streamlit on Streamlit Cloud  
- Push code to GitHub and deploy via **Streamlit Cloud**.  

---

💡 Future Enhancements  
🔹 User Authentication (JWT-based auth).  
🔹 Real-time Chat via WebSocket.  
🔹 Support for Multiple AI Models.  
🔹 Improved UI/UX for Chat Display.  

---

🐜 License
This project is licensed under MIT License.  

---

