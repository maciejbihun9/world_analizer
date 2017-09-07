
import unittest
from src.stock.stock_web_crawler import StockWebCrawler

class StockWebCrawlerTest(unittest.TestCase):

    def setUp(self):
        stock_name = "TSLA"
        self.stockWebCrawler = StockWebCrawler(stock_name)

    # TESTED
    def test_get_stock_summary(self):
        stock_summary = self.stockWebCrawler.get_stock_summary()
        print("Stock summary: ".format(stock_summary))

    # TESTED
    def test_get_stock_stats(self):
        stock_stats = self.stockWebCrawler.get_stock_stats()
        print("Stock stats: ".format(stock_stats))

    # TODO
    def test_get_stock_financials(self):
        stock_fin = self.stockWebCrawler.get_stock_financials()
        print("Stock financials: ".format(stock_fin))

    def test_stock_page_exists(self):
        stock_name = "ASB.WS"
        self.assertFalse(StockWebCrawler.stock_page_exists(stock_name))

    def test_get_stock_news(self):
        self.stockWebCrawler.get_stock_news()

