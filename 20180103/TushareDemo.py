import tushare as ts
import pandas as pd
import datetime

f = open('../data/stocks.txt')
time1 = datetime.datetime.now()
stocks = [line.strip() for line in f.readlines()]
dw = 880
data1 = ts.get_realtime_quotes(stocks[0:dw])
data2 = ts.get_realtime_quotes(stocks[dw:2 * dw])
data3 = ts.get_realtime_quotes(stocks[2 * dw, 3 * dw])
data4 = ts.get_realtime_quotes(stocks[3 * dw, -1])
time2 = datetime.datetime.now()
print(str(time1))
print(str(time2))
print(data1)
print(data2)
print(data3)
print(data4)
