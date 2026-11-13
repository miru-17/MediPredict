from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["healthanalyserdb"]
users_collection = db["users"]

print("✅ Connected to healthanalyserdb → users collection")
