from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["healthanalyserdb"]

predictions_collection = db["predictions"]
predictions_collection.insert_one({
    "test": "connection successful"
})

print("✅ Database + collection confirmed")
predictions_collection.insert_one({
    "test": "connection successful"
})

print("✅ Database + collection confirmed")

