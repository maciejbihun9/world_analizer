
from numpy import *
import logging


class Analizer():

    """
    Analizer should be executed by many threads.
    We can split our data on couple segments.
    Run 5 segemnts and submit that 5 segemnts
    """

    def __init__(self, comps_data, comp_method):
        self.comps_data = comps_data
        self.comp_method = comp_method
        logging.basicConfig(level=logging.DEBUG,
                            format='(%(threadName)-10s) %(message)s')

    def analize(self):
        stocks_corealtions = {}
        counter = 0
        for comp_one_data in self.comps_data:
            stocks_corealtions[comp_one_data[0][-1]] = {}
            for comp_two_data in self.comps_data:
                if comp_one_data[0][-1] == comp_two_data[0][-1]:
                    continue
                comparison_results = self.comp_method(comp_one_data, comp_two_data)
                stocks_corealtions[comp_one_data[0][-1]][comp_two_data[0][-1]] = comparison_results
                counter += 1
            print("Company parsed: {}".format(comp_one_data[0][-1]))
        return stocks_corealtions


