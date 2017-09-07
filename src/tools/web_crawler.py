from urllib import request
from bs4 import BeautifulSoup


class WebCrawler:

    def __init__(self, url):
        f = request.urlopen(url)
        html = str(f.read())
        print(html)
        self.soup = BeautifulSoup(html, "html.parser")

    def get_values_for_class(self, class_name) -> list:
        """
        Returns string items in list between tags with class = class_name
        """
        class_items = self.soup.find_all(attrs={'class': class_name})
        class_items_values = []
        for class_item in class_items:
            class_item_value = class_item.text.strip()
            class_items_values.append(class_item_value)
        return class_items_values

    def get_tags_with_class(self, class_name: str):
        """
        Returns tags that contains class_name.
        """
        return self.soup.find_all(attrs={'class': class_name})

    def get_values_for_tag(self, tag_name: str):
        """
        Returns string values between tag = tag_name.
        """
        tag_items = self.soup.find_all(tag_name)
        tag_item_values = []
        for tag_item in tag_items:
            tag_item_value = tag_item.text.strip()
            tag_item_values.append(tag_item_value)
        return tag_item_values

    def get_table_row_values(self):
        """
        Returns values from all rows in a table.
        """
        tag_items = self.soup.find_all("tr")
        table_rows = []
        for tag_item in tag_items:
            tag_child_item_values = tag_item.find_all("td")
            tag_item_child_values = []
            for tag_child_item_value in tag_child_item_values:
                tag_item_child_values.append(tag_child_item_value.text.strip())
            table_rows.append(tag_item_child_values)
        return table_rows

    def get_tags(self, tag_name: str):
        """
        Returns ResultSet with all tags with given name.
        """
        return self.soup.find_all(tag_name)


