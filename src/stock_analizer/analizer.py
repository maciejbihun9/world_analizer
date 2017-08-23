
from numpy import *
import logging

class Analizer():

    """
    Analizer should be executed by many threads.
    We can split our data on couple segments.
    Run 5 segemnts and submit that 5 segemnts
    """

    def __init__(self, comp_data, comp_method):
        self.comp_data = comp_data
        self.comp_method = comp_method
        logging.basicConfig(level=logging.DEBUG,
                            format='(%(threadName)-10s) %(message)s',
                            )
    """
    def analize(self):
        # split the data
        # comp_data_len = len(self.comp_data)
        # chunk_size = int(comp_data_len / num_of_workers)
        splited_data = []
        for i in range(0, comp_data_len, chunk_size):
            splited_data.append(self.comp_data[i:i + chunk_size])
        if len(splited_data[-1]) < chunk_size / 4:
            splited_data[-2].extend(splited_data[-1])
            del splited_data[-1]
    """

    def analize(self):
        stocks_corealtions = {}
        counter = 0
        for part_data_item in self.comp_data:
            stocks_corealtions[part_data_item[0][-1]] = {}
            for comp_data_item in self.comp_data:
                if part_data_item[0][-1] == comp_data_item[0][-1]:
                    continue
                comparison_results = self.comp_method(part_data_item, comp_data_item)
                stocks_corealtions[part_data_item[0][-1]][comp_data_item[0][-1]] = comparison_results
                logging.debug(
                    "Corelation results for {} : {} for {} : {}".format(comp_data_item[-1], comparison_results, counter,
                                                                        len(comp_data)))
                counter += 1
            logging.debug("Company parsed: {}".format(comp_data_item[0][-1]))
        return stocks_corealtions


