import pymongo
from pymongo import MongoClient
import warnings

class MongoDataManager:
    """
    Manages communication between algorithm and mongoDB database instance.
    """

    # MONGODB MANAGER EXCEPTION MESSAGES
    COLLECTION_DOES_NOT_EXISTS = "Collection does not exists."
    COLLECTION_EXISTS = "Collection already exists."

    def __init__(self, database: str):
        # make a connection to the localhost
        client = MongoClient('localhost', 27017)
        #  access database
        self.db = client[database]

    def create_collection(self, collection: str, indexes: list):
        """
        Creates collection if not exists one and sets indexes for it.
        :param collection: collection name as string
        :param indexes: collection indexes as string list
        """
        # if collection already exists
        if collection in self.db.collection_names():
            raise Exception(MongoDataManager.COLLECTION_EXISTS)
        self.db.create_collection(collection)
        # create indexes for a new collection
        for index in indexes:
            self.create_index(collection, index)

    def save_item(self, collection: str, item: dict):
        """
        Saves dict item(that figures as a json) to specified database
        :param collection: collection name from given database
        :param item: json item object to save
        """
        if collection not in self.db.collection_names():
            raise Exception(MongoDataManager.COLLECTION_DOES_NOT_EXISTS)
        self.db[collection].insert(item)

    def get_items(self, collection: str, query: dict) -> list:
        """
        Retrives an item from given collection using given key
        :return: Returns None if there is no object with given credentials.
        """
        matching_items = self.db[collection].find(query)
        items = []
        for item in matching_items:
            items.append(item)
        return items

    def create_index(self, collection: str, attr: str):
        self.db[collection].create_index([(attr, pymongo.ASCENDING)], unique = True)

    def get_colls_list(self):
        """
        Returns list with database collections.
        """
        return self.db.collection_names()

    def get_coll_count(self, collection: str) -> int:
        """
        Returns number of objects in the collection.
        """
        return self.db[collection].count()
