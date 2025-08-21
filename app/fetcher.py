from pymongo import MongoClient
import pandas as pd
import os

class MongoDAL:
    def __init__(self, uri: str = None, db_name: str = "IranMalDB"):

        self.uri = 'mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/'
        self.db_name = db_name

        # חיבור ל-Mongo
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
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

    # def insert_record(self, record: dict):
    #     """הוספת מסמך חדש"""
    #     res = self.collection.insert_one(record)
    #     return str(res.inserted_id)
    #
    # def get_records_as_dataframe(self, limit: int = 10):
    #     """שליפה כ-DataFrame"""
    #     docs = self.get_records(limit)
    #     return pd.DataFrame(docs) if docs else pd.DataFrame()
    #
    # def get_summary(self, limit: int = 100):
    #     """אנליזה בסיסית"""
    #     df = self.get_records_as_dataframe(limit)
    #     if df.empty:
    #         return {"rows": 0, "metrics": []}
    #     summary = (
    #         df.groupby("metric")
    #           .agg(count=("value","count"),
    #                mean=("value","mean"),
    #                min=("value","min"),
    #                max=("value","max"))
    #           .reset_index()
    #           .to_dict(orient="records")
    #     )
    #     return {"rows": len(df), "metrics": summary}
    #
    # def export_to_csv(self, limit: int = 100, filename: str = "export.csv"):
    #     """יצוא ל-CSV"""
    #     df = self.get_records_as_dataframe(limit)
    #     if df.empty:
    #         return "No data"
    #     df.to_csv(filename, index=False)
    #     return filename
    #


# a = MongoDAL(
# )
# print(a.get_records())