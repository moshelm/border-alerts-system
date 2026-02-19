from pymongo import MongoClient
import os 

MONGO_HOST = os.getenv("MONGO_HOST","localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT","27017"))
MONGO_DATABASE = os.getenv("MONGO_DATABASE","db_border")
MONGO_COLLECTION = os.getenv("MONGO_DATABASE","coll_border")

client = MongoClient(host= MONGO_HOST, port=MONGO_PORT)
database = client[MONGO_DATABASE]
collection = database[MONGO_COLLECTION]
