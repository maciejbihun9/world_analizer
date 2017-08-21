
from numpy import *
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import threading
import logging


def ana_ana(part_data, index, comp_data, comp_method):
    logging.debug("Thread {} started : {}".format(threading.currentThread().getName(), index))
    stocks_corealtions = {}
    counter = 0
    for part_data_item in part_data:
        stocks_corealtions[part_data_item[0][-1]] = {}
        for comp_data_item in comp_data:
            if part_data_item[0][-1] == comp_data_item[0][-1]:
                continue
            comparison_results = comp_method(part_data_item, comp_data_item)
            stocks_corealtions[part_data_item[0][-1]][comp_data_item[0][-1]] = comparison_results
            logging.debug("Corelation results for {} : {} for {} : {}".format(comp_data_item[-1], comparison_results, counter, len(comp_data)))
            counter += 1
        logging.debug("Company parsed: {}".format(comp_data_item[0][-1]))
    return stocks_corealtions

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

    def analize(self, num_of_workers):

        # split the data
        comp_data_len = len(self.comp_data)
        chunk_size = int(comp_data_len / num_of_workers)
        splited_data = []
        for i in range(0, comp_data_len, chunk_size):
            splited_data.append(self.comp_data[i:i + chunk_size])
        if len(splited_data[-1]) < chunk_size / 4:
            splited_data[-2].extend(splited_data[-1])
            del splited_data[-1]
        pool = multiprocessing.Pool(processes=2)
        pool.map(ana_ana, (self.comp_data, 2, self.comp_data, self.comp_method))

        executor = ThreadPoolExecutor(max_workers=num_of_workers)
        future_tasks = []
"""
        threads = []
        for index, part_data in enumerate(splited_data):
            t = threading.Thread(name="thread : " + str(index), target=ana_ana, args=(part_data, index, self.comp_data, self.comp_method))
            threads.append(t)
            t.start()

        for part_data in splited_data:
            # run task on seperate thread
            # future_tasks.append(executor.submit(self.ana_ana(part_data)))
            executor.submit(self.ana_ana(part_data))
            print("method executed")
        for future_tasks in future_tasks:
            print("Task results : {}".format(future_tasks.result()))

        """

