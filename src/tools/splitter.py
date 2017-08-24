import collections

class Splitter:
    """
    Splits the data into different sized chunks
    """
    @staticmethod
    def split_list_of_dicts_by(dicts_list: list, attr_name: str) -> collections.defaultdict:
        """
        :param dict_list: list of dicts
        :param attr_name: dict attribute name
        :return: splitted data dict by attribute name
        """
        result = collections.defaultdict(list)
        for d in dicts_list:
            result[d[attr_name]].append(d)
        return result