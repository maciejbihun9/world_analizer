from numpy import *
from datetime import datetime

class Converter:

    NOT_PROPERLY_FORMATTED = "Date not properly Formatted. It has to be like '2012-04-22'"

    """
    Json methods
    """
    @staticmethod
    def lists_to_json(items: list, cols_names_types: dict) -> str:
        """
        Maps all data with that titles.
        :param: items: list of list with string items.
        :param: cols_names_types: dict with column names and types
        """
        json_items = []
        for item in items:
            json_item = {}
            for item_feature_value, column in zip(item, cols_names_types):
                json_item[column] = item_feature_value
            json_items.append(json_item)
        return json_items

    @staticmethod
    def json_to_ndarray(dict_object) -> ndarray:
        days_prices = []
        for day_prices in dict_object:
            days_prices.append(list(day_prices.values())[1:])
        return array(days_prices)

    """
    Date methods
    """
    @staticmethod
    def string_to_date(date: str) -> datetime:
        """
        Date string has to be in format -> '2015-10-20'
        """
        try:
            dt = datetime.strptime(date, '%Y-%m-%d')
        except:
            raise Exception(Converter.NOT_PROPERLY_FORMATTED)
        return dt

