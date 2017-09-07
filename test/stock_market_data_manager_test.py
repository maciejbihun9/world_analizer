
import unittest
from src.stock.stock_market_data_manager import StockMarketDataManager

class StockMarketDataManagerTest(unittest.TestCase):

    def setUp(self):
        self.stockMarketDataManager = StockMarketDataManager()

    # Test it only with filled stock collection.
    def test_load_stocks(self):
        stock_names = ["RVP", "ROX", "ROC", "RWC", "SACH"]
        loaded_stocks = self.stockMarketDataManager.load_stocks(stock_names)
        self.assertTrue(len(loaded_stocks) == 4)

        stock_names = []
        loaded_stocks = self.stockMarketDataManager.load_stocks(stock_names)
        self.assertTrue(len(loaded_stocks) is not 0)
        self.assertTrue(type(loaded_stocks[0]) is dict)

