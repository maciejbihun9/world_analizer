from src.stock.stock_saver import StockSaver
from src.stock.stock_companies import *
from src.stock.stock_market_data_manager import StockMarketDataManager
from src.stock.stock_web_crawler import StockWebCrawler
from src.tools.web_crawler import WebCrawler

stockSaver = StockSaver()

sub_amex_comps = amex_comps[100:]

sub_amex_comps_summaries = []
for sub_amex_comp in sub_amex_comps:
    # omit stocks that are not noted in yahoo
    if not StockWebCrawler.stock_page_exists(sub_amex_comp):
        print("Stock: {} is not noted in yahoo". format(sub_amex_comp))
        continue
    stockWebCrawler = StockWebCrawler(sub_amex_comp)
    stock_summary = stockWebCrawler.get_stock_summary()
    stockSaver.save_stock(stock_summary)
    print("{} summary has been parsed.".format(sub_amex_comp))
