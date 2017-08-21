from datetime import datetime
import pandas_datareader.data as web

now_time = datetime.now()

start_time = datetime(now_time.year - 5, now_time.month, now_time.day)

f_dat = web.DataReader('NASDAQ:TSLA', 'google', start_time, now_time)

print(f_dat)
