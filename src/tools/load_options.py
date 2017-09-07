import pandas_datareader as data
from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockPricesDataManager
import datetime

start = datetime.datetime(2000, 1, 1)

# end = datetime.datetime(2013, 1, 27)

now = datetime.datetime.now()

# companies = ['AGN', 'ADS', 'LNT', 'ALL', 'GOOGL', 'GOOG']

companies = StockPricesDataManager.get_s_and_p_names()

StockPricesDataManager.load_options(companies)