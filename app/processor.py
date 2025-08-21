import pandas
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
nltk.download('/usr/local/share/nltk_data')  # Compute sentiment labels

class Process:
    def __init__(self  , df):
        self.df = df
        self.list_weapon = self.get_list_weapon("../data/weapon_list.txt")
    def add_most_common_word_colomn(self):
        self.df["rarest_word"] = self.df['Text'].transform(lambda x : self.get_rarest_word_word(text=x ))

    def add_emotion_of_text_colomn(self):
        self.df['sentiment'] = self.df['Text'].transform(lambda x : self.find_emotion_of_text(x))

    def add_personal_weapon(self):
        self.df["weapons_detected"] = self.df['Text'].transform(lambda text : self.find_weapond_from_list(text,self.list_weapon))

    def rename_culomn(self , name_to_change , name_to_be_changed):
        self.df.rename({name_to_change:name_to_be_changed} , axis = 1 , inplace=True)

    @staticmethod
    def get_rarest_word_word(text):
        split_text = text.split()
        d = {}
        for element in split_text:
            if element in d:
                d[element] += 1
            else:
                d[element] = 1
        max_word = min(d, key=d.get)
        return max_word


    @staticmethod
    def find_emotion_of_text(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        emotion = score['compound']
        if  1 > emotion  > 0.5 :
            return "positive"
        elif 0.5 > emotion > -0.5 :
            return "neutral"
        elif -0.5 > emotion > -1 :
            return "negative"
        else:
            return "?"
    @staticmethod
    def get_list_weapon(path):
        nested_array = pandas.read_csv(path)
        return np.array(nested_array).flatten()

    @staticmethod
    def find_weapond_from_list(text , lst):
        for word in text.split():
            if word.lower() in  lst:
                return word
        return "No"








# f = fetcher.MongoDAL()
# df = f.get_records()
# a = Process(df)
# a.add_most_common_word_colomn()
# print(a.df[["Text" , "Most_common_word"]])
# print(a.df["Text"].loc[4])
# print(a.df.columns)
# m = a.get_most_common_word("RT @IDF: The last 24 hours in Israel: https://t.co/0YNwvMsYvL")
# print(m)

# Import dependencies
# a.add_emotion_of_text_colomn()
# print(a.df[["Text" , "emotion"]])
# print(a.list_weapon)
# a.add_personal_weapon()
# print(a.df[["Text" , "weapons_detected"]].sort_values(by="weapons_detected"))
# a.rename_culomn("Text" , "original_text")
# a.rename_culomn("_id" , "id")
# print(a.df.columns)
# print(a.df[["Text" , "weapons_detected"]].sort_values(by="weapons_detected"))
# print(a.df)