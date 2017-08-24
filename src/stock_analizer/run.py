
from src.stock_analizer.analizer import Analizer
from src.tools.converter import Converter
from src.stock_analizer.google_finance.stock_analisis.stock_comparator import StockComparator
from concurrent.futures import ThreadPoolExecutor
from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockPricesDataManager
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

stockDataManager = StockPricesDataManager(database)

companies = ['NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'PCAR']

start_date = "2015-05-20"

start_date = Converter.string_to_date(start_date)

end_date = "2015-10-20"

end_date = Converter.string_to_date(end_date)

# load 10 companies between dates
analisis_data = stockDataManager.load_comps_data_btn_dates(stock_collection, companies, start_date, end_date)

analisis_data = Splitter.split_list_of_dicts_by(analisis_data, "Name")

analisis_data = list(analisis_data.values())

converted_data = []
for analise_data in analisis_data:
    converted_data.append(Converter.json_to_ndarray(analise_data))


analizer = Analizer(converted_data, StockComparator.cor_comp)
results = analizer.analize()
print(results)

