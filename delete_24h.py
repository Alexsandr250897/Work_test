from pymongo import MongoClient
from datetime import datetime, timedelta, timezone


class MongoTTLManager:
    def __init__(self, db_name, collection_name, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_document_with_expiry(self, data, expire_hours=24):
        expire_at = datetime.now(timezone.utc) + timedelta(hours=expire_hours)
        document = data
        document['expireAt'] = expire_at
        self.collection.insert_one(document)
        print(f"Документ добавлен: {document}")

    def create_ttl_index(self):
        self.collection.create_index('expireAt', expireAfterSeconds=0)
        print("TTL-индекс создан.")


if __name__ == "__main__":
    ttl_manager = MongoTTLManager(db_name='my_database', collection_name='my_collection')
    ttl_manager.add_document_with_expiry(data={'data': 'example_data'}, expire_hours=24)
    ttl_manager.create_ttl_index()
