import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    conn.commit()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,100)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
             (unix, date, keyword, value))
    conn.commit()

def close_database_connection():
    c.close()
    conn.close()

def read_from_database():
    c.execute("SELECT * from stuffToPlot")
    for row in c.fetchall():
        print(row)

def graph_representation():
    c.execute("SELECT datestamp, value from stuffToPlot")
    data = c.fetchall()

    dates = []
    values = []
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])
    print(dates)
    plt.plot_date(dates, values, '-')
    plt.show()

create_table()
##data_entry()

for i in range(10):
    time.sleep(1)
    dynamic_data_entry()
read_from_database()

graph_representation()
close_database_connection()
