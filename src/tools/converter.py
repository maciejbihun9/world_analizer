from numpy import *
from datetime import datetime
from dateutil.parser import parse


class Converter:

    NOT_PROPERLY_FORMATTED = "Date not properly Formatted. It has to be like '2012-04-22'"

    """
    --------------------------------------------------------------------------------------------------------------------
    CONVERT METHODS    
    --------------------------------------------------------------------------------------------------------------------
    """
    @staticmethod
    def lists_to_json(items: list, cols_names_types: list) -> str:
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

    @staticmethod
    def string_with_commas_to_float(item: str):
        return float(item.replace(',', ''))


    """
    --------------------------------------------------------------------------------------------------------------------
    CHECKS METHODS    
    --------------------------------------------------------------------------------------------------------------------
    """
    @staticmethod
    def is_date(item: str) -> bool:
        """
        Checks if string item is a date
        """
        try:
            float(item)
            return False
        except:
            try:
                parse(item)
                return True
            except ValueError:
                return False

    @staticmethod
    def is_empty_str(item: str) -> bool:
        """
        Checks if an item is a n empty string.
        """
        return not bool(len(item))

    @staticmethod
    def is_number(item: str) -> bool:
        """
        Checks if string value is a number
        """
        try:
            float(item)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_number_with_commas(item) -> bool:
        """
        Checks if string value is float number with commas
        """
        # if contains commas between numbers
        splitted_item = item.split(",")
        first_last_items = [splitted_item[0], splitted_item[-1]]
        try:
            list(map(float, first_last_items))
            return True
        except:
            return False


