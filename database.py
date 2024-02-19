import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_db():
    uri = os.environ.get("MONGO_DB_ATLAS_URI")
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
    except Exception as e:
        raise(e)

    return client['clinic']

def read_data(db: MongoClient, collection_name: str, **kwargs): # TODO: put kwargs to select data
    collection = db[collection_name]
    return collection.find(kwargs)


if __name__ == "__main__":
    db = get_db()
    data = read_data(db, 'schedule')
    
    for d in data:
        print(type(d))
        print(d)