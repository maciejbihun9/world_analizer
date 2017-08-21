
from src.tools.mongo_data_manager import MongoDataManager

s_and_p_database = "s_and_p_companies"

stock_database = "stock"

s_and_p_DataManager = MongoDataManager(s_and_p_database)

stockDataManager = MongoDataManager(stock_database)

db_colls_names = s_and_p_DataManager.get_colls_list()

for coll in db_colls_names:
    coll_items = s_and_p_DataManager.get_items(coll, {})
    # write it to the stock database
    print(coll_items)

    # create coll dict item

    comp_obj = {"name" : coll, "stock_prices" : coll_items}

    stockDataManager.save_item("NYSE", comp_obj)
    print("Companies parsed: {}".format(coll))

