import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fani
from matplotlib import style
import matplotlib.ticker as mticker
import time
from random import randrange

startTime = time.time()
title='Kawaii Desssu'
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animateThis(i):
    inputFile = open('exampleFile.csv','r')
    graph_data = inputFile.read()
    lines = graph_data.split('\n')
    x = []
    y = []
    newX =str(len(lines))
    newY = str(randrange(10))
    for line in lines:
        if len(line) > 1:
            xs, ys = line.split(',')
            x.append(float(xs))
            y.append(float(ys))
    inputFile.close()
    ax1.clear()
    ax1.plot(x, y)
    ax1.set_title(title)
    ax1.yaxis.set_major_locator(mticker.MultipleLocator(1))## ticks are located at the multiple of 1
    ## This code sets a new line in the input file, so that the next iteration have new data
    writer = open('exampleFile.csv','a')
    writer.write(newX+','+newY+'\n')
    writer.close()
    

ani = fani(fig, animateThis, interval=1000)
plt.show()


