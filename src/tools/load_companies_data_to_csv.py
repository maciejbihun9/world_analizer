from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockDataManager
from datetime import datetime
from src.tools.json_parser import JsonParser
from src.tools.data_manager import DataManager

folder = "../../resources/stock_data/"

stock_name = 'NYSE'

stock_companies = StockDataManager.get_s_and_p_names()

start_date = datetime(2010, 8, 19)

end_date = datetime.now()

StockDataManager.stocks_data_to_csv(stock_name, stock_companies, start_date, end_date, folder)