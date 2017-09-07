from pandas_datareader import data
from datetime import datetime
from src.tools.data_manager import DataManager
import pandas as pd
from numpy import *

class Adjuster:
    """
    Adjusts the data for processing
    """
    @staticmethod
    def data_weekends_and_miss_data_adj(data_reader: data.DataReader, start_date: datetime, end_date: datetime, comp_name: str) -> data.DataReader:
        features_adjusted = 0
        all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
        list_attrs = ["Open", "High", "Low", "Close", "Volume", "Name"]
        data_frame = pd.DataFrame(index = all_weekdays, columns=list_attrs)
        for list_attr in list_attrs:
            if list_attr == "Name":
                data_frame[list_attr] = comp_name
                continue
            attr = data_reader.ix[list_attr]
            attr = attr.reindex(all_weekdays)
            adj_attr = attr.fillna(method='ffill')
            attr_values = adj_attr.get_values()
            data_frame[list_attr] = attr_values
        return data_frame

