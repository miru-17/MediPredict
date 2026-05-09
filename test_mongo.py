from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["healthanalyserdb"]

print("✅ Connected to MongoDB successfully")
