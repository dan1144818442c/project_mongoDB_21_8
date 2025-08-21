import processor
import fetcher
import json

class Manager:
    def __init__(self, uri: str = None, db_name: str = "IranMalDB"):
        self.df = fetcher.MongoDAL().get_records()
        self.process = processor.Process(df=self.df)
    def add_and_rename_coloumn(self):
        self.process.add_personal_weapon()
        self.process.add_emotion_of_text_colomn()
        self.process.add_most_common_word_colomn()
        self.process.rename_culomn("Text", "original_text")
        self.process.rename_culomn("_id", "id")
        self.process.df = self.df.drop('TweetID', axis=1)
        return self.process.df

    def get_df_as_list_of_json(self):
        df = self.add_and_rename_coloumn()
        json_lst = []
        for i in range(len(df)):
            d = json.loads(df.iloc[i, :].to_json())
            json_lst.append(d)
        return json_lst

# m = manager()
# df = m.add_and_rename_coloumn()
# print(m.get_df_as_list_of_json()[1])

