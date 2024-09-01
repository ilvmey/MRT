from pymongo import MongoClient

import os

USERNAME = os.getenv('MONGO_INITDB_ROOT_USERNAME')
PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)

client = None

def get_client():
    global client
    if client is None:
        client = MongoClient(f'mongodb://{USERNAME}:{PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/')
        return client

    return client