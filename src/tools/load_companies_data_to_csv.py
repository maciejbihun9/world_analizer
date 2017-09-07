from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockPricesDataManager
from datetime import datetime
from src.tools.converter import Converter
from src.tools.data_manager import DataManager

folder = "../../resources/Stock Data/Company Prices/"

stock_name = 'NYSE'

# stock_companies = ['BDX', 'BRK.B', 'BBY', 'BIIB', 'BLK', 'HRB', 'BA', 'BWA', 'BXP', 'BSX', 'BHF', 'BMY']

stock_companies = StockPricesDataManager.get_s_and_p_names()

start_date = datetime(2013, 7, 19)

end_date = datetime.now()

StockPricesDataManager.stocks_data_to_csv(stock_name, stock_companies, start_date, end_date, folder)





