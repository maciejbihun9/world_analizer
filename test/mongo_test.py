
import unittest
from src.tools.mongo_data_manager import MongoDataManager
import pymongo


class MongoTest(unittest.TestCase):

    def setUp(self):
        """
        Set up the environment for the tests
        """
        database = "test"
        indexes = ["Date"]
        self.user_collection = "users"
        self.mongoDataManager = MongoDataManager(database, indexes)

    def test_get_item(self):
        """
        Tests getting items from the database
        """
        users = self.mongoDataManager.get_items(self.user_collection, "Date", 2015)
        self.assertTrue(len(users) != 0)
        users = self.mongoDataManager.get_items(self.user_collection, "Date", 2016)
        self.assertTrue(len(users) == 0)

    def test_index(self):
        """
        Tests if indexing mechanizm works well for collections.
        """
        test_obj = {"Date" : 2015, "user" : "Maciej"}
        # check if object already exists in the database
        objects = self.mongoDataManager.get_items(self.user_collection, "Date", 2015)
        if len(objects) == 0:
            self.mongoDataManager.save_item(self.user_collection, test_obj)
        # save object that already exist and watch if method throws an exception.
        with self.assertRaises(pymongo.errors.DuplicateKeyError):
            self.mongoDataManager.save_item(self.user_collection, test_obj)

