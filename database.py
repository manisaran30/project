import urllib
from pymongo import MongoClient # type: ignore
from urllib.parse import quote_plus  # Import for encoding

# Your MongoDB credentials
password = "@x5X7Z7XzcnJ3a6aw"  # Replace with your actual password
encoded_password = urllib.parse.quote_plus(password)

MONGO_URI = f"mongodb+srv://1234:{encoded_password}@cluster0.kcg9qyn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Establish connection
client = MongoClient(MONGO_URI)

# Select database and collection
db = client["your_database_name"]  # Replace with actual database name
collection = db["your_collection_name"]  # Replace with actual collection name

# database.py
def get_chat_summary(chat_id):
    # Your function logic here
    return "Chat Summary Placeholder"


def store_chat(user_id, conversation_id, message):
    """Store chat messages in MongoDB."""
    chat_data = {
        "user_id": user_id,
        "conversation_id": conversation_id,
        "message": message
    }
    collection.insert_one(chat_data)  # Insert into MongoDB
