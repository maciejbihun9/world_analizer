
from src.tools.mongo_data_manager import MongoDataManager
from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockPricesDataManager
from src.tools.converter import Converter
import os
import datetime
# save csv files to the database

folder = '../../resources/Company Data/'

stock_database = "stock"

stock_prices = "stock_prices"

stockDataManager = StockPricesDataManager(stock_database)

cols_names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name']

# for each file in the folder
for filename in os.listdir(folder):
    if filename.endswith("_data.csv"):
        print("file from folder: {}".format(filename))
        comp_url = folder + filename
        comp_data = StockPricesDataManager.load_company_data(comp_url)
        json_data = Converter.lists_to_json(comp_data, cols_names)
        print(json_data)
        stockDataManager.save_comp(stock_prices, json_data)




