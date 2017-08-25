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
    def data_weekends_and_miss_data_adj(data_reader: data.DataReader, start_date: datetime, end_date: datetime, ) -> data.DataReader:

        panel_name = data_reader["Name"]
        features_adjusted = 0
        all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
        list_attrs = ["Open", "High", "Low", "Close", "Volume", "Name"]
        data_frame_attr_values = []
        # zbieranie danych w pętli oraz utworzenie macierzy danych
        for list_attr in list_attrs:
            # attr values
            attr = data_reader.ix[list_attr]
            attr = attr.reindex(all_weekdays)

            attr_values = attr.get_values()
            data_frame_attr_values.append(attr_values)
        data_frame_attr_values = asarray(data_frame_attr_values).T.tolist()

        # create a dataframe object
        data_frame = pd.DataFrame(data_frame_attr_values, index = all_weekdays, columns=list_attrs)

        for index in range(len(list_attrs)):
            attr = data_reader.ix[list_attrs[index]]
            attr = attr.reindex(all_weekdays)
            dataFrame[list_attrs[index]] = pd.Series(attr.get_values())
            # adj_attr = data_reader.ix['Adj ' + str(list_attrs[index])]
            # adj_attr = adj_attr.fillna(method='ffill')
            features_adjusted += 1
            print("features adjusted : {}".format(features_adjusted))
        DataManager.create_Data_Frame()
        return data_reader



