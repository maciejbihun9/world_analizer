
from datetime import datetime
from pandas import DataFrame
import pandas_datareader.data as web
from src.tools.mongo_data_manager import MongoDataManager
from numpy import *
import os


class StockDataManager:
    """
    Manages company data writing and reading.
    """

    PRICE_COLLECTION = "stock_prices"

    def __init__(self, database: str):
        self.mongoDataManager = MongoDataManager(database)
        self.collection = StockDataManager.PRICE_COLLECTION

    @staticmethod
    def load_company_data(company: str):
        """
        Loads data from csv file into numpy ndarray
        :param company: company name as string
        """
        prices = []
        url = '../../../resources/google_s_and_p/'
        file_name = company + '_data.csv'
        url += file_name
        file = open(url)
        next(file)
        for line in file.readlines():
            line_elements = line.strip().split(',')
            if '' in line_elements:
                continue
            else:
                prices.append(array([str(line_elements[0]) ,float(line_elements[1]), float(line_elements[2]), float(line_elements[3]), float(line_elements[4]), float(line_elements[5])], dtype=object))
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
            try:
                company_df = web.DataReader(stock_name + ':{0}'.format(company), 'google', start_date, end_date)
                company_df['Name'] = company
                stock_companies_size = len(stock_companies)
                output_name = folder + company + '_' + str(stock_companies_size) + '_' + str(start_date.year) + '_' + str(end_date.year) + '_data.csv'
                company_df.to_csv(output_name)
                print("{} : parsed".format(company))
            except:
                not_parsed.append(company)
                continue
        print("Companies not parsed: {}".format(not_parsed))

    def stocks_data_to_mongo(self, collection: str, json_items: str):
        """
        Saves data from csv files into mongo db.
        After parsing, removes data from the folder.
        """
        self.mongoDataManager.save_item(collection, json_items)

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
        Saves one or many stock day prices
        """
        self.mongoDataManager.save_item(comp_name, comp_data)

    def load_comp_data(self, comp_name):
        """
        Loads all data associated with specified company
        """
        items = self.mongoDataManager.get_items(comp_name, None, None)

    def load_comp_data_in_range(self, comp_name: str, start_data: datetime, end_date: datetime):
        """
        Loads comp data between specified dates range.
        """
        query = {"Name" : comp_name}
        self.mongoDataManager.get_items(self.collection, query)
        db.items.find({"age" : {$gte:30}})

