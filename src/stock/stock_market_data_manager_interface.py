from abc import ABCMeta, abstractmethod
from datetime import datetime

class StockDataManagerInterface:
    __metaclass__ = ABCMeta

    @classmethod
    def create_stocks_collection(self):
        """
        Creates stocks collection with specified fields and validator
        """

    @classmethod
    def create_stocks_stats_collection(self):
        """
        Creates stocks stats collection with specified fields and validator
        """

    @classmethod
    def load_stocks(self):
        """
        Returns dicts list with all stocks.
        """

    @classmethod
    def save_stocks(self, stocks: list):
        """
        Saves or updates stocks as dicts in the database.
        In this project one stock object is a collection
        of summary attributes from Yahoo finance.
        """

    @staticmethod
    def stock_exists(self, stock_name: str):
        """
        Checks if given stock name exists in the database.
        """

    #TODO
    @staticmethod
    def update_stock(self, stock_name: str, ):
        """
        If stock exists then update object's values.
        """

    @staticmethod
    def replace_stock(self, stock_name, stock: dict):
        """
        Replaces stock object that exists in the database with given stock_name.
        """


    @classmethod
    def load_stock_by_attr(self, attr_name: str):
        """
        Returns stocks dict list with specified attribute name.
        """

    @classmethod
    def load_stocks_with_dividend(self):
        """
        Returns all stocks with dividend values.
        """

    @classmethod
    def load_day_prices_btn_dates(self, stock_name: str, start_date: datetime, end_date: datetime):
        """
        Returns Close stock prices and volumen btn dates.
        """

    @classmethod
    def load_minute_prices_btn_dates(self, stock_name: str, start_date: datetime, end_date: datetime):
        """
        Returns minute stock prices and volumen btn dates.
        """

    @classmethod
    def load_hour_prices_btn_dates(self, stock_name: str, start_date: datetime, end_date: datetime):
        """
        Returns hour stock prices and volumen btn dates.
        """

    @classmethod
    def load_news_btn_dates(self, stock_name: str, start_date: datetime, end_date: datetime):
        """
        Returns news for stock between dates.
        """

