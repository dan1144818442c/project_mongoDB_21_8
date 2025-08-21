import pandas
import fetcher
class Process:
    def __init__(self ):
        self.df = fetcher.MongoDAL().get_records()

    def add_most_common_word_colomn(self):

