
from numpy import *
"""
Method should have one responsibility,
Jakie parametry:
* data do analizowania wraz z opisem typu tych danych 
* if we want to test it we have to parse data from the file -> that is ok, because either way 
we should have to create a method to prepare this data.
* doing this we create a coupling between downloading data and analising it.
* we should download it before method call
"""
def analize(stock_data: ):
    """
    Analizes the data under different points.
    We can pick stock comparator technique to analize our data
    """
    stocks_corealtions = {}
    s_and_p_names = StockDataManager.get_s_and_p_names()
    for s_and_p_name_1 in s_and_p_names:
        try:
            stock_data_1 = StockDataManager.load_company_data(s_and_p_name_1)
        except Exception:
            continue
        for s_and_p_name_2 in s_and_p_names:
            if s_and_p_name_1 == s_and_p_name_2:
                continue
            try:
                stock_data_2 = StockDataManager.load_company_data(s_and_p_name_2)
            except:
                continue
            if len(stock_data_2) == 0:
                print(0)
            stocks_corr = StockComparator.cor_comp(stock_data_1, stock_data_2)
            vol_ratio = StockComparator.vol_ratio_comp(stock_data_1, stock_data_2)
            stocks_corealtions["{} : {}".format(s_and_p_name_1, s_and_p_name_2)] = stocks_corr
            print("corelations: {} : {} - value: {} ".format(s_and_p_name_1, s_and_p_name_2, stocks_corr))
            print("volumens: {} : {} - value: {} ".format(s_and_p_name_1, s_and_p_name_2, vol_ratio))
analize(None, None)
