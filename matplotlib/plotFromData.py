import matplotlib.pyplot as plt
import csv
import datetime as dt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style
style.use("ludduman")

print(plt.style.available)
##Candlestick charts need to be made with different module now, skip for this tutorial (2 Mar 2021)
x = []
y = []

## open file with csv module
##with open('exampleFile.csv','r') as csvfile:
##    plots = csv.reader(csvfile, delimiter=',')
##    for row in plots:
##        x.append(int(row[0]))
##        y.append(int(row[1]))

## open file using numpy
##x,y = np.loadtxt('exampleFile.csv', delimiter=',', unpack=True)
##
##
##plt.plot(x,y, label='Loaded from file!')
##plt.xlabel('x')
##plt.ylabel('y')
##plt.title('Interesting Graph\nCheck it out')
##plt.legend()
##plt.show()

def decodeAndDateTime(byteStr):
    return dt.datetime.fromisoformat(byteStr.decode('utf-8'))


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(stock_price_url).read().decode()
stock_data = []
split_source = source_code.split('\n')
for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)

##date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
##                                                      delimiter=',',
##                                                      unpack=True,
##                                                      # %Y = full year. 2015
##                                                      # %y = partial year 15
##                                                      # %m = number month
##                                                      # %d = number day
##                                                      # %H = hours
##                                                      # %M = minutes
##                                                      # %S = seconds
##                                                      # 12-06-2014
##                                                      # %m-%d-%Y
##                                                      converters={0: bytespdate2num('%Y-%m-%d')})

date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                  dtype = {'names':('date', 'closep', 'highp', 'lowp', 'openp', 'adj_closep', 'volume'),
                                                                                'formats':('|S15', np.float, np.float, np.float, np.float, np.float, np.float)},
                                                                  delimiter=',',
                                                                  unpack=True)

dateConv = np.vectorize(decodeAndDateTime)
date = dateConv(date)

ax1 = plt.subplot2grid((1,1), (0,0))
titleName = "TSLA"

ax1.plot_date(date, closep, '-', label="Price")
for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
ax1.grid(True)
##ax1.xaxis.label.set_color('c')
##ax1.yaxis.label.set_color('r')
ax1.set_yticks([0,100,200,300, 400, 500, 600, 700, 800, 900, 1000])
ax1.fill_between(date, closep, closep[0],where=(closep >= closep[0]), facecolor='g', alpha=0.5, label='Gain')
ax1.fill_between(date, closep, closep[0],where=(closep < closep[0]), facecolor='r', alpha=0.8, label='Loss')
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

ax1.spines['left'].set_color('c')
ax1.spines['left'].set_linestyle((0,(20,40)))
ax1.spines['top'].set_visible(False)
ax1.tick_params(axis='x', colors='#f06215')
ax1.axhline(closep[0], color='#666666')


plt.xlabel('Date')
plt.ylabel('Price')
plt.title(titleName)
plt.legend()
plt.show()
