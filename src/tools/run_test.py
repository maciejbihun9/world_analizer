from datetime import datetime
from src.tools.mongo_data_manager import MongoDataManager
from src.stock_analizer.google_finance.stock_analisis.stock_data_manager import StockPricesDataManager
from src.stock_analizer.google_finance.stock_analisis.analize_data_manager import AnalizeDataManager

from src.tools.converter import Converter
import pymongo

database = "stock"

mongoDataManager = MongoDataManager(database)

stockDataManager = StockPricesDataManager(database)

analizeDataManager = AnalizeDataManager(database)

stock_collection = "stock_prices"

start_date = "2014-05-20"

start_date = Converter.string_to_date(start_date)

end_date = "2015-10-20"

end_date = Converter.string_to_date(end_date)

# test queries
# query = {'Name': "MMM", "Date" : {'$gte': start_date, '$lt': end_date}}
# query = {"Name" : "MMM", "Volume" : 1830929.0}
# query = {"Name" : "MMM", "Volume" : {"$gte" : 3000000}}
# results = stockDataManager.load_comp_data_btn_attr_values("MMM", "Open", 113, 116)
# query = {"$or":[ {"Name":"NSC"}, {"Name":"MMM"}]}
# yourmongocoll.find({"$and":[ {"vals":100}, {"vals":1100}]})
# query = {"$and" : [{"$or":[ {"Name":"NSC"}, {"Name":"MMM"}]} , {"Date" : {"$gte": start_date, "$lt" : end_date}}]}
# query = {"$and" : [{"$or":[ {"Name":"NSC"}, {"Name":"MMM"}]} , {"Date" : {"$gte": start_date, "$lt" : end_date}}]}


results = analizeDataManager.load_analisis("corelation")
print(results)

