import pandas_datareader as data

import datetime

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2013, 1, 27)

now = datetime.datetime.now()

f = data.DataReader(["OGZPY", "XOM"], 'yahoo-dividends', start, now)
dividends = f["Dividends"]

print(dividends)