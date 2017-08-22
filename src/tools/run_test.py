from datetime import datetime
from src.tools.mongo_data_manager import MongoDataManager
import pymongo


datetime_object = datetime.strptime('30-01-12', '%d-%m-%y').date()

mongoDataManager = MongoDataManager("test")

collection = "test_col"

obj = {"date" : datetime_object}

mongoDataManager.save_item(collection, obj)

