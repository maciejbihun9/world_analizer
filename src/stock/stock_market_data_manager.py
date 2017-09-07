from src.stock.stock_market_data_manager_interface import StockDataManagerInterface
from src.tools.mongo_data_manager import MongoDataManager
import src.properties as pr
from pymongo import MongoClient
from src.tools.data_manager import DataManager
import os


class StockMarketDataManager(MongoDataManager, StockDataManagerInterface):
    """
    Manages data operations between stock database in the cloud and application.
    """
    STOCKS_COLLECTION = "stocks"

    STATS_COLLECTION = "stats"

    FINS_COLLECTION = "fins"

    DATABASE = "stock_market"

    def __init__(self):
        mongo_client = MongoClient('mongodb://%s:%s@%s:%s' % (pr.username, pr.password, pr.host, pr.port))
        MongoDataManager.__init__(self, self.DATABASE, mongo_client)

    def stock_exists(self, stock_name: str) -> bool:
        return self.item_exists(self.STOCKS_COLLECTION, {"Name": stock_name})

    def replace_stock(self, stock_name: str, stock: dict):
        self.replace_item(self.STOCKS_COLLECTION, {"Name": stock_name}, stock)

    def create_stocks_collection(self):
        self.create_collection(self.STOCKS_COLLECTION, ["Name"])

    def load_stocks(self, stock_names: list) -> list:
        """
        Loads stocks with given names or all when list is empty.
        If stock name is not in database then method does not returns anything.
        :param: stock_names list with stock names to get.
        """
        if len(stock_names) is not 0:
            query = {"$or": [{"Name": stock_name} for stock_name in stock_names]}
        else:
            query = {}
        return self.load_items(self.STOCKS_COLLECTION, query)

    def save_stocks(self, stocks):
        """
        :param stocks: list with stock object as dicts or just one dict object.
        Saves stock objects into the stocks collection.
        """
        self.save_items(self.STOCKS_COLLECTION, stocks)

    @staticmethod
    def load_comp_names_from_dir(url: str):
        """
        Load companies from files in directory under url.
        """
        for file_name in os.listdir(url):
            file = open(url+file_name)
            companies = []
            for line in file.readlines():
                line = line.split("\n")
                companies.append(line[0])
            print(companies)




