from numpy import *
import json

class JsonParser:

    @staticmethod
    def parse_lists_to_json(items: list, column_names: list) -> str:
        """
        Maps all data with that titles.
        :param: items: list of list with string items.
        """
        json_items = []
        for item in items:
            json_item = {}
            for index, item_feature_value in enumerate(item):
                json_item[column_names[index]] = item_feature_value
            json_items.append(json_item)
        return json_items

    @staticmethod
    def json_to_ndarray(json_object) -> ndarray:
        comp_prices = json_object["stock_prices"]
        days_prices = []
        for day_prices in comp_prices:
            days_prices.append(list(day_prices.values())[1:])
        return array(days_prices)

