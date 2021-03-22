from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.ticker as mticker
import numpy as np
import random as rn


fig = plt.figure()

def createData():
    x = []
    y = []

    for i in range(10):
        x.append(i)
        y.append(rn.randrange(10))

    return x, y
# adding subplot with add_subplot

ax1 = fig.add_subplot(337) ## 3x3 plot grid like analogue phone keypad, with plot in 7 position
ax2 = fig.add_subplot(339) ## 3x3 plot grid like analogue phone keypad, with plot in 9 position
ax3 = fig.add_subplot(311) ## 3x1 plot grid like 3 lines, with plot in 1st position

x1, y1 = createData()
ax1.plot(x1, y1)
ax1.set_title('AX1')
x2, y2 = createData()
ax2.plot(x2, y2)
ax2.set_title('AX2')
x3, y3 = createData()
ax3.plot(x3, y3)
ax3.set_title('AX3')
fig.tight_layout() # add this after plotting the data


# adding sub plot using subplot2grid
fig1 = plt.figure()
bx3 = plt.subplot2grid((6,1), (4,0), rowspan=2, colspan=1)
bx1 = plt.subplot2grid((6,1), (0,0), rowspan=2, colspan=1, sharex = bx3, sharey = bx3)
bx2 = plt.subplot2grid((6,1), (2,0), rowspan=2, colspan=1, sharex = bx3, sharey = bx3)

bx3.xaxis.set_major_locator(mticker.MultipleLocator(1))
## Y axis ticks are not constant, it's [0,5] or [2.5, 5, 7.5], changing this here
bx3.yaxis.set_major_locator(mticker.MultipleLocator(1))

bx3TwinX = bx3.twinx() ##creates a new copy of x axis with an y axis to the other side
#with different range(default 0->1 may be) and ticks
bx3TwinX.axes.set_ylim(0,9)## I need to set the y axis range explicitly
bx3TwinX.yaxis.set_major_locator(mticker.MultipleLocator(1))
## one way of changing tick size
bx1.tick_params(axis='y', labelsize=8, color='m')
bx2.tick_params(axis='y', labelsize=8, color='m')
bx3.tick_params(axis='y', labelsize=8, color='m')
bx3TwinX.tick_params(axis='y', labelsize=8, color='g')

bx1.plot(x1, y1)
bx1.set_title('BX1')
bx2.plot(x2, y2)
bx2.set_title('BX2')
## to show sharex shares unnecessary range- bx1, bx2 don't have x=11 value
x3.append(11)
y3.append(rn.randrange(10))
bx3.plot(x3, y3)
bx3.set_title('BX3')
fig1.tight_layout()
plt.show()
