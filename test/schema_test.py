
import unittest
from src.tools.mongo_data_manager import MongoDataManager

class SchemaTest(unittest.TestCase):

    def test_schema(self):
        database = "stock"
        collection = "NYSE"
        mongoDataManager = MongoDataManager(database)
        col_items = mongoDataManager.load_items(collection, {"name" : "ABC"})
        print(col_items)
