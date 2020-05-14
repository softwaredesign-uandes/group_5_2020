import pymongo
import sys
sys.path.append('..')
from controllers.block import Block
from controllers.publisher import Publisher

class DBProvider(Publisher):
    def __init__(self):
        Publisher.__init__(self)
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mines"]
        self.collection = None
    
    def select_collection(self, block_model_name):
        collection = self.db[block_model_name] 
        self.collection = collection
        return collection

    def load_blocks(self, path, name_data_set, columns_names):
        blocks_file = open(path, "r")
        blocks = []
        for block_row in blocks_file:
            block_data = block_row.strip().split(" ")
            block = Block(columns_names, block_data)
            block.save_in_database(self.collection)
            blocks.append(block)
        self.notify("loaded-blocks")
        return blocks
    def clear_collection(self, block_model_name):
        collection = self.db[block_model_name] 
        collection.drop()
        self.collection = self.db[block_model_name] 
        return collection

