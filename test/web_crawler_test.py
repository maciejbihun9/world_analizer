from src.tools.web_crawler import WebCrawler
import unittest


class WebCrawlerTest(unittest.TestCase):
    def setUp(self):
        web_page_url = "https://finance.yahoo.com/quote/NFLX/financials?p=NFLX"
        self.web_crawler = WebCrawler(web_page_url)

    def test_get_values_from_class(self):
        class_name = "Fz(s) H(35px) Va(m)"
        class_item_values = self.web_crawler.get_values_for_class(class_name)
        print(class_item_values)

    def test_get_items_with_class(self):
        class_name = "Fz(s) H(35px) Va(m)"
        class_item_values = self.web_crawler.get_tags_with_class(class_name)
        print(class_item_values)

    def test_get_list_values(self):
        web_page_url = "https://finance.yahoo.com/quote/NFLX/"
        web_crawler = WebCrawler(web_page_url)
        class_name = "Mb(0) Ov(h) P(0) Wow(bw)"
        items = web_crawler.get_tags_with_class(class_name)
        print(items)

    def test_get_tag_items(self):
        tag_name = "span"
        tag_item_values = self.web_crawler.get_values_for_tag(tag_name)
        print(tag_item_values)

    def test_get_table_row_values(self):
        results = self.web_crawler.get_table_row_values()
        print(results)

    def test_get_tags(self):
        tag_name = "span"
        tags = self.web_crawler.get_tags(tag_name)
        print(tags)

