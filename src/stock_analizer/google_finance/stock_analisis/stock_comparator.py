
from numpy import *

class StockComparator:

    @staticmethod
    def cor_comp(stock_prices_1: ndarray, stock_prices_2: ndarray) -> float:
        """
        We have to change it to be list of dicts with dates.
        :param stock_prices_1:
        :param stock_prices_2:
        :return:
        """
        correlations = []
        stock_prices_by_dates = dict()
        com_dates = list(set(stock_prices_1[:, 0]).intersection(stock_prices_2[:, 0]))
        if len(stock_prices_1) == len(stock_prices_2):
            for stock_price_1, stock_price_2 in zip(stock_prices_1, stock_prices_2):
                corel = corrcoef(array(stock_price_1[1:5], dtype=float), array(stock_price_2[1:5], dtype=float)).tolist()[0][1]
                correlations.append(corel)
            coef = sum(correlations) / len(correlations)
        else:
            for com_date in com_dates:
                stock_prices_by_dates[com_date] = [[], []]

            for stock_price_1 in stock_prices_1:
                if stock_price_1[0] in com_dates:
                    stock_prices_by_dates[stock_price_1[0]][0] = stock_price_1[1:5]
            for stock_price_2 in stock_prices_2:
                if stock_price_2[0] in com_dates:
                    stock_prices_by_dates[stock_price_2[0]][1] = stock_price_2[1:5]
            for stock_price_by_date in stock_prices_by_dates:
                try:
                    corel = corrcoef(array(stock_prices_by_dates[stock_price_by_date][0], dtype=float),
                                     array(stock_prices_by_dates[stock_price_by_date][1], dtype=float)).tolist()[0][1]
                except:
                    continue
                    print(stock_price_by_date)
                if isnan(corel):
                    corel = 0
                correlations.append(corel)
            coef = sum(correlations) / len(correlations)
        return coef

    @staticmethod
    def vol_ratio_comp(stock_vols_1: ndarray, stock_vols_2: ndarray) -> float:
        """
        Computes difference between volumen's
        Takes ndarray with date & date_vol as a row's
        """
        com_dates = list(set(stock_vols_1[:, 0]).intersection(stock_vols_2[:, 0]))
        stock_vols_by_dates = dict()
        for com_date in com_dates:
            stock_vols_by_dates[com_date] = [[], []]

        for stock_vol_1 in stock_vols_1:
            if stock_vol_1[0] in com_dates:
                stock_vols_by_dates[stock_vol_1[0]][0] = stock_vol_1[-1]
        for stock_vol_2 in stock_vols_2:
            if stock_vol_2[0] in com_dates:
                stock_vols_by_dates[stock_vol_2[0]][1] = stock_vol_2[-1]

        vols_ratio = []
        for stock_vol_by_date in stock_vols_by_dates:
            max_vol = max(stock_vols_by_dates[stock_vol_by_date])
            min_vol = min(stock_vols_by_dates[stock_vol_by_date])
            vol = min_vol / max_vol
            vols_ratio.append(vol)
        vol_ratio_coef = sum(vols_ratio) / len(vols_ratio)
        return vol_ratio_coef









