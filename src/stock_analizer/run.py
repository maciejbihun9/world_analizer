
from src.stock_analizer.analizer import Analizer
from src.tools.mongo_data_manager import MongoDataManager
from src.tools.json_parser import JsonParser
from src.stock_analizer.google_finance.stock_analisis.stock_comparator import StockComparator
from concurrent.futures import ThreadPoolExecutor

database = "stock"

collection = "NYSE"

# load tha data from the database
stockDataManager = MongoDataManager(database)

stock_comps = stockDataManager.get_items(collection, {})

obj = {
    "date" : ISODate()
}

# parse the data to ndarray -> json paresr
stock_comps_list = []
for stock_comp in stock_comps:
    stock_comps_list.append(JsonParser.json_to_ndarray(stock_comp))

analizer = Analizer(stock_comps_list, StockComparator.cor_comp)
results = analizer.analize(5)

"""
executor = ThreadPoolExecutor(max_workers=5)
future = executor.submit(analizer)
results= future.result()
print(results)
"""




