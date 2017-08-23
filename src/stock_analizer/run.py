
from src.stock_analizer.analizer import Analizer
from src.tools.converter import Converter
from src.stock_analizer.google_finance.stock_analisis.stock_comparator import StockComparator
from concurrent.futures import ThreadPoolExecutor
from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockPricesDataManager
from src.tools.converter import Converter


"""
In run we run all methods associated with analisis
"""

database = "stock"

analisis_collection = "analisis"

stock_collection = "stock_prices"


# loda data fro analisis

stockDataManager = StockPricesDataManager(database)

companies = ['PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM']

start_date = "2015-05-20"

start_date = Converter.string_to_date(start_date)

end_date = "2015-10-20"

end_date = Converter.string_to_date(end_date)

# load 10 companies between dates
analisis_data = stockDataManager.load_comps_data_btn_dates(stock_collection, companies, start_date, end_date)

analisis_data = Converter.json_to_ndarray(analisis_data)

analizer = Analizer(analisis_data, StockComparator.cor_comp)
results = analizer.analize()
print(results)

