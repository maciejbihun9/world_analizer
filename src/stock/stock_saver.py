from src.stock.stock_market_data_manager import StockMarketDataManager


class StockSaver:

    def __init__(self):
        self.stockDataManager = StockMarketDataManager()

    def save_stock(self, stock: dict):
        """
        Saves stock summary
        :param: dict object with stock attributes.
        """
        self.stockDataManager.save_stocks(stock)
