import pymongo
from pymongo import MongoClient
import warnings
import logging

class MongoDataManager:
    """
    Manages communication between algorithm and mongoDB database instance.
    # CREATE A MONGO CLIENT
    # mongo_client = MongoClient('mongodb://%s:%s@%s:%s' % (username, password, host, port))
    # mongo_client = MongoClient("127.0.0.1", 27017)
    """

    # MONGODB MANAGER EXCEPTION MESSAGES
    COLLECTION_DOES_NOT_EXISTS = "Collection does not exists."
    COLLECTION_EXISTS = "Collection already exists."

    def __init__(self, database: str, client: MongoClient):
        # make a connection to the localhost
        self.mongo_db_logger = logging.getLogger("DB logger")
        self.mongo_db_logger.setLevel(logging.INFO)
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
        print("Collection: {} has been created".format(collection))

    def replace_item(self, collection: str, attrs: dict, new_item: dict):
        """
        Replaces item and returns weather replacement was successfull.
        """
        write_results = self.db[collection].update(attrs, new_item)
        return bool(write_results["n"])

    def item_exists(self, collection: str, query: dict) -> bool:
        """
        Checks if item exists in specified collection.
        """
        return bool(self.db[collection].count(query))

    def save_items(self, collection: str, items: list):
        """
        Saves dict item(that figures as a json) to specified database
        :param collection: collection name from given database
        :param items: list of json(dict) object to save.
        """
        if collection not in self.db.collection_names():
            raise Exception(MongoDataManager.COLLECTION_DOES_NOT_EXISTS)
        try:
            self.db[collection].insert(items)
        except Exception as e:
            logging.error(e)

    def load_items(self, collection: str, query: dict) -> list:
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
