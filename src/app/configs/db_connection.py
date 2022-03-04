from app.configs.config import MONGO_HOST, MONGO_PORT, MONGO_DATABASE
from pymongo import MongoClient


client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}')
db_connection = client[MONGO_DATABASE]
