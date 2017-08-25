
from datetime import datetime
from pandas import DataFrame
from src.tools.mongo_data_manager import MongoDataManager
from datetime import datetime
from src.stock_analizer.yahoo_finance.adjuster import Adjuster
from src.tools.converter import Converter
from pandas_datareader import data
import pandas as pd
from numpy import *
import sys
import os


class StockPricesDataManager(MongoDataManager):
    """
    Manages company data writing and reading.
    """

    PRICE_COLLECTION = "stock_prices"

    def __init__(self, database: str):
        MongoDataManager.__init__(self, database)
        self.collection = StockPricesDataManager.PRICE_COLLECTION

    @staticmethod
    def load_company_data(url: str):
        """
        Loads data from csv file into numpy ndarray
        :param company: company name as string
        """
        prices = []
        file = open(url)
        next(file)
        for line in file.readlines():
            line_elements = line.strip().split(',')
            if '' in line_elements:
                continue
            else:
                prices.append(array([Converter.string_to_date(line_elements[0]) ,float(line_elements[1]), float(line_elements[2]), float(line_elements[3]), float(line_elements[4]), float(line_elements[5]), str(line_elements[6])], dtype=object))
        return array(prices)

    @staticmethod
    def stocks_data_to_csv(stock_name: str, stock_companies: list, start_date: datetime, end_date: datetime, folder: str):
        """
        Retrives stock data and saves into database with the same name.
        :param company: stock name as a str from we want to get the data.
        :param stock_companies: stock companies names as strings
        """
        not_parsed = []
        for i, company in enumerate(stock_companies):
                # company_df = data.DataReader(stock_name + ':{0}'.format(company), 'finance', start_date, end_date)
                company_df = data.DataReader([company], 'yahoo', start_date, end_date)
                company_df = Adjuster.data_weekends_and_miss_data_adj(company_df, start_date, end_date)
                company_df['Name'] = company
                stock_companies_size = len(stock_companies)
                output_name = folder + company + '_' + str(stock_companies_size) + '_' + str(start_date.year) + '_' + str(end_date.year) + '_data.csv'
                company_df.to_csv(output_name)
                print("{} : parsed".format(company))
        print("Companies not parsed: {}".format(not_parsed))

    def stocks_data_to_mongo(self, collection: str, json_items: str):
        """
        Saves data from csv files into mongo db.
        After parsing, removes data from the folder.
        """
        self.save_item(collection, json_items)

    @staticmethod
    def get_s_and_p_names():
        """
        Returns list with all S&P companies names.
        """
        s_and_p = ['MMM', 'ABT', 'ABBV', 'ACN', 'ATVI', 'AYI', 'ADBE', 'AMD', 'AAP', 'AES',
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
                   'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', 'EVHC', 'EOG', 'EQT', 'EFX',
                   'EQIX', 'EQR', 'ESS', 'EL', 'ES', 'RE', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'EXR', 'XOM',
                   'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FISV', 'FLIR', 'FLS', 'FLR',
                   'FMC', 'FL', 'F', 'FTV', 'FBHS', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GD', 'GE', 'GGP',
                   'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GS', 'GT', 'GWW', 'HAL', 'HBI', 'HOG', 'HRS', 'HIG',
                   'HAS', 'HCA', 'HCP', 'HP', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON',
                   'HRL', 'HST', 'HPQ', 'HUM', 'HBAN', 'IDXX', 'INFO', 'ITW', 'ILMN', 'IR', 'INTC', 'ICE',
                   'IBM', 'INCY', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'SJM',
                   'JNJ', 'JCI', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KHC',
                   'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LKQ', 'NYSE:LMT',
                   'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT',
                   'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'KORS', 'MCHP', 'MU', 'MSFT', 'MAA',
                   'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MYL', 'NDAQ', 'NOV', 'NAVI',
                   'NTAP', 'NFLX', 'NYSE:NWL', 'NFX', 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NYSE:NBL',
                   'JWN',
                   'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'PCAR',
                   'PKG', 'PH', 'PDCO', 'PAYX', 'PYPL', 'PNR', 'PBCT', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM',
                   'PSX', 'PNW', 'PXD', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU',
                   'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RRC', 'RJF', 'RTN', 'O', 'RHT', 'REG',
                   'REGN', 'RF', 'RSG', 'RMD', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RCL', 'CRM', 'SCG', 'SLB', 'SNI',
                   'STX', 'SEE', 'SRE', 'SHW', 'SIG', 'SPG', 'SWKS', 'SLG', 'SNA', 'SO', 'LUV', 'SPGI', 'SWK', 'SPLS',
                   'SBUX', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYF', 'SNPS', 'SYY', 'TROW', 'TGT', 'TEL', 'FTI',
                   'TXN', 'TXT', 'TMO', 'TIF', 'TWX', 'TJX', 'TMK', 'TSS', 'TSCO', 'TDG', 'TRV', 'TRIP', 'FOXA',
                   'FOX', 'TSN', 'UDR', 'ULTA', 'USB', 'UA', 'UAA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UTX', 'UHS',
                   'UNM', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT',
                   'WBA', 'DIS', 'WM', 'WAT', 'WEC', 'WFC', 'HCN', 'WDC', 'WU', 'WRK', 'WY', 'WHR', 'WFM', 'WMB',
                   'WLTW', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
        return s_and_p

    def save_comp(self, comp_name, comp_data):
        """
        Saves company data
        """
        self.save_item(comp_name, comp_data)

    def load_comp_data(self, collection: str, comp_name: str):
        """
        Loads all data associated with specified company
        """
        query = {"Name" : comp_name}
        return self.get_items(collection, query)

    def load_comps_data_btn_dates(self, collection: str, comp_names: list, start_date: datetime, end_date: datetime):
        """
        Loads all data associated with specified companies.
        """
        mongoDataManager = MongoDataManager("stock")
        if start_date == None or end_date == None:
            comp_names = [{"Name": comp_name} for comp_name in comp_names]
            # query = {"$or": [{"Name": "NSC"}, {"Name": "MMM"}]}
            query = {"$or": comp_names}
        else:
            comp_names = [{"Name": comp_name} for comp_name in comp_names]
            query = {"$and" : [{"$or": comp_names}, {"Date" : {"$gte": start_date, "$lt" : end_date}}]}
        return self.get_items(collection, query)

    def load_comp_data_btn_dates(self, comp_name: str, start_date: datetime, end_date: datetime):
        """
        Loads company data between specified date range.
        """
        query = {'Name': comp_name, "Date" : {'$gte': start_date, '$lt': end_date}}
        return self.get_items(self.collection, query)

    def load_comp_data_btn_attr_values(self, comp_name: str, attr: str, min: float, max: float):
        """
        Loads company data that's between specified range.
        """
        query = {'Name': comp_name, attr : {'$gte': min, '$lt': max}}
        return self.get_items(self.collection, query)

    def load_comp_data_btn_vals_and_dates(self, comp_name: str, attr: str, start_date: datetime, end_date: datetime, min: float, max: float):
        """
        Loads company data that's between specified range and between dates.
        """
        query = {'Name': comp_name, attr : {'$gte': min, '$lt': max}}
        self.get_items(self.collection, query)
