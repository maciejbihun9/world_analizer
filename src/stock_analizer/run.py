
from src.stock_analizer.analizer import Analizer
from src.tools.converter import Converter
from src.stock_analizer.google_finance.stock_analisis.stock_comparator import StockComparator
from concurrent.futures import ThreadPoolExecutor
from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockPricesDataManager
from src.stock_analizer.google_finance.stock_analisis.analize_data_manager import AnalizeDataManager

from src.tools.converter import Converter
from src.tools.splitter import Splitter
import collections

"""
In run we run all methods associated with analisis
"""

database = "stock"

analisis_collection = "analisis"

stock_collection = "stock_prices"


# loda data fro analisis

analizeDataManager = AnalizeDataManager(database)

stockDataManager = StockPricesDataManager(database)

companies = ['MMM', 'ABT', 'ABBV', 'ACN', 'ATVI', 'AYI', 'ADBE', 'AMD', 'AAP', 'AES',
                   'AET', 'AMG', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALXN', 'ALGN', 'ALLE',
                   'AGN', 'ADS', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP',
                   'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'ANDV', 'ANSS',
                   'ANTM', 'AON', 'AOS', 'APA', 'AIV', 'AAPL', 'AMAT', 'ADM', 'ARNC', 'AJG', 'AIZ', 'T',
                   'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BHGE', 'BLL', 'BAC', 'BK', 'BCR', 'BAX', 'BBT',
                   'BDX', 'BRK.B', 'BBY', 'BIIB', 'BLK', 'HRB', 'BA', 'BWA', 'BXP', 'BSX', 'BHF', 'BMY',
                   'AVGO', 'BF.B', 'CHRW', 'CA', 'COG', 'CPB', 'COF', 'CAH', 'CBOE', 'KMX', 'CCL', 'CAT',
                   'CBG', 'CBS', 'CELG', 'CNC', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHTR', 'CHK', 'CVX',
                   'CMG', 'CB', 'CHD', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX',
                   'CME', 'CMS', 'COH', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'CXO', 'COP', 'ED',
                   'STZ', 'COO', 'GLW', 'COST', 'COTY', 'CCI', 'CSRA', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR',
                   'DRI', 'DVA', 'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DLR', 'DFS', 'DISCA', 'DISCK', 'DISH',
                   'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE', 'DRE', 'DD', 'DUK', 'DXC', 'ETFC', 'EMN',
                   'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', 'EVHC', 'EOG', 'EQT', 'EFX']

start_date = "2013-08-20"

start_date = Converter.string_to_date(start_date)

end_date = "2017-08-20"

end_date = Converter.string_to_date(end_date)

# load 10 companies between dates
analisis_data = stockDataManager.load_comps_data_btn_dates(stock_collection, companies, start_date, end_date)

analisis_data = Splitter.split_list_of_dicts_by(analisis_data, "Name")

analisis_data = list(analisis_data.values())

converted_data = []
for analise_data in analisis_data:
    converted_data.append(Converter.json_to_ndarray(analise_data))

analizer = Analizer(converted_data, StockComparator.cor_comp)
analisis_results = analizer.analize()

analisis_col_types = ["Type", "start_date", "end_date", 'comps', 'corelations']
analisis_item = [["corelation", start_date, end_date, companies, analisis_results]]

analisis_results = Converter.lists_to_json(analisis_item ,analisis_col_types)

analizeDataManager.save_analisis(analisis_results)

print(analisis_results)

