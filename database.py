import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MONGO_DB_ATLAS_PASSWORD = os.environ.get("MONGO_DB_ATLAS_PASSWORD")
uri = f"mongodb+srv://psiqguilhermeletsch:{MONGO_DB_ATLAS_PASSWORD}@my-clinic.kcqzquv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)