import pymongo
import sys


def DbProvider(self):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mines"]
    
    def create_collection(self, block_model_name):
        collection = self.db[block_model_name] 
        return collection
