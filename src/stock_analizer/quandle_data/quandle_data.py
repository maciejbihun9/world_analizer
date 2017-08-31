import pandas_datareader.data as web

symbol = 'EIA/AEO_2016_REF_NO_CPP_PRCE_NA_COMM_NA_NG_NA_NA_Y13DLRPMCF_A'  # or 'AAPL.US'

df = web.DataReader(symbol, 'quandl', "1965-01-01", "2017-08-25")

print(df)


