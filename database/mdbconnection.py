from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

# MongoDB Connection
client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    tlsAllowInvalidCertificates=True  # ← Ithu must aanu Mac nu
)
try:
    client.admin.command("ping")
    print("MongoDB Connected Successfully!")
except Exception as e:
    print("MongoDB Connection Error:", e)

db = client["football_database"]
players_collection = db["players"]