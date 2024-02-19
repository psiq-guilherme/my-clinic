import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_db():
    uri = os.environ.get("MONGO_DB_ATLAS_URI")
    # uri = "mongodb+srv://psiqguilhermeletsch:icuX44H0nY7NpGXm@my-clinic.kcqzquv.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
    except Exception as e:
        raise(e)

    return client

if __name__ == "__main__":
    client = get_db()
    print(client)