
from src.tools.web_crawler import WebCrawler
from dateutil.parser import parse
from src.tools.converter import Converter
from src.stock.stock_signs import StockSigns
import logging

class StockWebCrawler():

    def __init__(self, stock_name: str):
        self.stock_name = stock_name
        self.base_url = "https://finance.yahoo.com"

    @staticmethod
    def stock_page_exists(stock_name: str) -> bool:
        """
        Checks if given stock exists in yahoo finance
        """
        url = "https://finance.yahoo.com/quote/%s?p=%s"%(stock_name, stock_name)
        crawler = WebCrawler(url)
        table_row_values = crawler.get_table_row_values()
        del table_row_values[0]
        return len(table_row_values) is not 0

    def __create_attr_dict(self, url: str):
        crawler = WebCrawler(url)
        table_row_values = crawler.get_table_row_values()
        del table_row_values[0]
        attr_dict = {}
        attr_dict["Name"] = self.stock_name
        for table_row_value in table_row_values:
            if len(table_row_value) == 1:
                continue
            parsed_values = self._attr_parser(table_row_value[1])
            if len(parsed_values) > 1:
                attr_dict[table_row_value[0] + " " + list(parsed_values[0].keys())[0]] = list(parsed_values[0].values())[0]
                attr_dict[table_row_value[0] + " " + list(parsed_values[1].keys())[0]] = list(parsed_values[1].values())[0]
            else:
                attr_dict[table_row_value[0]] = parsed_values[0]
        return attr_dict

    def get_stock_summary(self) -> dict:
        """
        Returns a dict with stock summaries.
        """
        url = "https://finance.yahoo.com/quote/%s?p=%s" % (self.stock_name, self.stock_name)
        summary_dict = self.__create_attr_dict(url)
        summary_dict["Average Volume"] = summary_dict["Avg. Volume"]
        del summary_dict["Avg. Volume"]
        return summary_dict

    def get_stock_stats(self):
        summary_url = self.url%("quote", self.stock_name, self.stock_name)
        url = "https://finance.yahoo.com/quote/%s/key-statistics?p=%s"%(self.stock_name, self.stock_name)
        stats_dict = self.__create_attr_dict(url)
        return stats_dict

    # TODO
    def get_stock_news(self):
        """
        There is a lot of things to think about.
        """
        news_url = "https://finance.yahoo.com/quote/%s?p=%s"%(self.stock_name, self.stock_name)
        news_list_class = "Mb(0) Ov(h) P(0) Wow(bw)"
        web_crawler = WebCrawler(news_url)
        items_with_class = web_crawler.get_tags_with_class(news_list_class)
        news_list = items_with_class[0]
        for news_item in news_list:
            # get link element from each news_item
            a_attrs = news_item.find("a").attrs
            article_link = a_attrs["href"]
            full_article_link = self.base_url + article_link
            article_web_crawler = WebCrawler(full_article_link)
            # get ul from this page

    # TODO
    def get_stock_financials(self):
        url = "https://finance.yahoo.com/quote/%s/financials?p=%s"%(self.stock_name, self.stock_name)
        fin_dict = self.__create_attr_dict(url)
        return fin_dict

    # refactor metody parsowania danych
    def _attr_parser(self, attr_value: str) -> list:
        # if attr_value is a number
        # check if attr_value is a number
        if Converter.is_number(attr_value):
            return [float(attr_value)]
        elif Converter.is_empty_str(attr_value):
            return [""]
        elif StockSigns.BRACKET in attr_value:
            first_part = attr_value.split("(")[0]
            if Converter.is_number(first_part):
                return [float(first_part)]
            else:
                return [""]
        elif StockSigns.PROCENT in attr_value:
            return [float(attr_value.split("%")[0])]
        elif StockSigns.NOT_AVAILABLE in attr_value:
            return [""]
        elif StockSigns.SPACED_LINE in attr_value:
            attr_values = attr_value.split(" - ")
            if Converter.is_date(attr_values[0]):
                return [parse(attr_values[0])]
            else:
                return [{"min" : float(attr_values[0])}, {"max" : float(attr_values[1])}]
        elif StockSigns.SPACED_X in attr_value:
            attr_values = attr_value.split(" x ")
            return [{"value" : float(attr_values[0])}, {"amount" : float(attr_values[1])}]
        elif StockSigns.LINE == attr_value:
            return [""]
        elif StockSigns.MILION in attr_value:
            attr_value = attr_value.split("M")[0]
            attr_value = float(attr_value)
            attr_value = attr_value * 1000000
            return [float(attr_value)]
        elif StockSigns.BILION in attr_value:
            attr_value = attr_value.split("B")[0]
            attr_value = float(attr_value)
            attr_value = attr_value * 1000000000
            return [float(attr_value)]
        elif Converter.is_number_with_commas(attr_value):
            return [Converter.string_with_commas_to_float(attr_value)]
        elif Converter.is_date(attr_value):
            return [parse(attr_value)]
        else:
            return [float(attr_value)]








