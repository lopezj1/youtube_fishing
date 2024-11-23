import os
from pymongo import MongoClient
from contextlib import contextmanager

MONGO_URI = os.environ['MONGO_URI']
MONGO_DB_NAME = os.environ['MONGO_DB_NAME']

@contextmanager
def mongodb_connection(mongo_uri=MONGO_URI, db_name=MONGO_DB_NAME):
    """Context manager to connect to MongoDB and handle teardown"""
    client = MongoClient(mongo_uri)
    db = client[db_name]
    try:
        yield db
    finally:
        client.close()

def insert_data(db, collection_name, data, group_field):
    """Inserts data into the specified MongoDB collection"""
    collection = db[collection_name]

    # Iterate through each group and insert its items
    for group_name, items in data.items():
        if isinstance(items, list):  # Ensure items is a list
            for item in items:
                if isinstance(item, dict):  # Ensure each item is a dictionary
                    # Add group information to the document
                    document = {group_field: group_name, **item}
                    result = collection.insert_one(document)
                    print(f"Inserted document for {group_field} '{group_name}' with _id: {result.inserted_id}")
        else:
            print(f"Skipped group '{group_name}' because it doesn't contain a list of items.")

def insert_categories(db, collection_name, data):
    collection = db[collection_name]

    document =  [{'id': item['id'], 'title': item['snippet']['title']} for item in data['items']]
    result = collection.insert_many(document)
    print("Inserted document for categories")
