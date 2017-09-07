from numpy import *
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn import linear_model, datasets, model_selection
import pandas as pd
import os
import glob


class DataManager:
    """
    Data Manager job is to load entire data.
    Data Manager does not care about data types.
    We can remove unused data items before specific tasks.
    We should not use here any patterns that not load specific signs.
    """

    @staticmethod
    def load_to_data_frame(url: str, index_col: str):
        """
        Loads the data from csv and excel files to DataFrame object.
        """
        data_frame = pd.read_csv(url, index_col=index_col, parse_dates=True)
        data_frame.fillna(method="ffill", inplace=True)
        data_frame.fillna(method="bfill", inplace=True)
        return data_frame

    @staticmethod
    def save_to_csv(url: str, data_frame: pd.DataFrame, index: bool):
        data_frame.to_csv(url, index = index)

    @staticmethod
    def load_data(url: str, miss_first_line: bool, do_convert: bool, split_sign: str) -> list:
        """
        :param url: file to parse url
        :param miss_first_line: miss first line bool value
        :param do_convert: Make conversion to convenient types
        :return: parsed data as data_list
        """
        file = open(url)
        if miss_first_line:
            next(file)
        data = []
        for line in file.readlines():
            line_elements = line.strip().split(split_sign)
            data_item = []
            for line_el_index in range(len(line_elements)):
                item = line_elements[line_el_index]
                try:
                    if do_convert:
                        item = float(line_elements[line_el_index])
                except:
                    pass
                data_item.extend([item])
            data.append(data_item)
        return data

    @staticmethod
    def order_data(inputs: ndarray, target: ndarray, task_classes: list) -> ndarray:
        """
        Return ndarray of lists of items sorted by category.
        :param inputs:
        :param target: ndarray with target classes represented as int numbers started from 0
        :param task_classes: list with available target classes.
        :return:
        """
        categorized_items = []
        for task_class in task_classes:
            categorized_items.append([])

        for inp_ind, input in enumerate(inputs):
            categorized_items[target[inp_ind]].append(input)
        categorized_items = array(categorized_items)
        for category in range(len(categorized_items)):
            categorized_items[category] = array(categorized_items[category])
        return categorized_items


    @staticmethod
    def categorize_data(data: ndarray, categorical_mask: list):
        """
        Split the data in to:
        - data_non_categoricals
        - data_categoricals
        Assign numerical values to labeled type values
        :param data: ndarray of data without targets
        :param categorical_mask: list with variable categories
        :return: data_non_categoricals, data_categoricals lists
        """
        enc = LabelEncoder()
        for i in range(0, data.shape[1]):
            if (categorical_mask[i]):
                label_encoder = enc.fit(data[:, i])
                print("Klasy kategorialne:", label_encoder.classes_)
                integer_classes = label_encoder.transform(label_encoder.classes_)
                print("Klasy całkowito-liczbowe:", integer_classes)
                t = label_encoder.transform(data[:, i])
                data[:, i] = t

        mask = ones(data.shape, dtype=bool)
        for i in range(0, data.shape[1]):
            if (categorical_mask[i]):
                mask[:, i] = False

        # non categorical data
        data_non_categoricals = data[:, all(mask, axis=0)]

        # categorical data
        data_categoricals = data[:, ~all(mask, axis=0)]

        hotenc = OneHotEncoder()

        hot_encoder = hotenc.fit(data_categoricals)
        encoded_hot = hot_encoder.transform(data_categoricals)

        new_data = append(data_non_categoricals, encoded_hot.todense(), 1)

        return array(new_data)

    @staticmethod
    def train_test_split(inputs: ndarray, target: ndarray, test_size: float, random_state: int):
        """
        :param inputs:
        :param target:
        :param test_size:
        :param random_state:
        :return: X_train, X_test, y_train, y_test ndarrays.
        """
        return model_selection.train_test_split(inputs, target, test_size=test_size, random_state=random_state)

    @staticmethod
    def data_filter(data: ndarray, filter_sign: str) -> ndarray:
        """
        Removes all rows that contains filter_sign.
        :param filter_sign:
        :return: New ndarray without unneeded data items(rows)
        """
        m, n = shape(data)
        inds_to_remove = []
        for i in range(m):
            for j in range(n):
                item = data[i, j]
                if type(item) is not str:
                    continue
                if item.strip() == filter_sign:
                    inds_to_remove.append(i)
                    break
        filtered_data = delete(data, inds_to_remove, 0)
        return array(filtered_data)

    @staticmethod
    def item_occurrences(data: ndarray) -> dict:
        """
        :param data: ndarray of data to count
        :return: dict with number of occurances of each data item.
        """
        u, counts = unique(data, return_counts=True)
        return dict(zip(u, counts))

    @staticmethod
    def assign_classes(target: ndarray) -> ndarray:
        # classes as set
        classes = {0}
        classes.remove(0)
        for target_item in target:
            classes.add(target_item)
        classes = list(classes)
        new_target = [0] * len(target)
        for target_index, target_item in enumerate(target):
            new_target[target_index] = classes.index(target_item)
        return array(new_target)

    @staticmethod
    def create_data_frame(data: ndarray, categories: list) -> dict:
        m, n = shape(data)
        # for each category
        data_dict = {}
        for i in range(n):
            data_dict[categories[i]] = data[:, i]
        # data_frame = pd.DataFrame(data_dict)
        return data_dict

    @staticmethod
    def clear_folder(folder_url: str):
        """
        Removes all files from folder
        """
        files = glob.glob(folder_url + "/*")
        for f in files:
            os.remove(f)

    @staticmethod
    def create_Data_Frame(data: ndarray, index: list, columns: list) -> pd.DataFrame:
        m,n = shape(data)
        if m != len(index):
            print("Indexes and the data not the same length.")
        if n != len(columns):
            print("Columns and the data not the same length.")
        return pd.DataFrame(data, index=index, columns=columns)

    @staticmethod
    def get_data_frame_values(data_frame: pd.DataFrame)->list:
        """
        Returns DataFrame values.
        """
        return data_frame.get_values()

    @staticmethod
    def get_data_frame_columns(data_frame: pd.DataFrame)-> list:
        """
        Returns DataFrame columns.
        """
        return list(data_frame.columns.values)

    @staticmethod
    def get_data_frame_indexes (data_frame: pd.DataFrame)-> list:
        """
        Returns DataFrame indexes.
        """
        return list(data_frame.index.values)

