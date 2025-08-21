from pymongo import MongoClient
import pandas as pd

class MongoDAL:
    def __init__(self, uri, db_name):
        # חיבור ל-Mongo
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.col_name = self.get_col_name()
        self.collection = self.db[self.col_name]

    def get_col_name(self):
        return self.db.list_collection_names()[0]



    def get_records(self, limit: int = 10):
        """שליפת מסמכים"""
        docs = list(self.collection.find().limit(limit))
        for d in docs:
            d["_id"] = str(d["_id"])
        return pd.DataFrame(docs)




