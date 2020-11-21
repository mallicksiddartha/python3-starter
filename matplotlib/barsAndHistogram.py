from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
x = [1, 2, 5, 6]
y = [7, 6, 4, 2]
x2 = [3,4, 7, 9]
y2 = [1, 8, 10, 16]
alpha = ['aa', 'ba', 'ca', 'da']
beta = ['xa', 'ya', 'za', 'wa']
#plt.plot(x, y)
#plt.plot(x2, y2)
'''
Bar chart - You have x number of different things and you have their corresponding heights
the first list is the X coordinates of the different things, the second list is the height of those different
things.
You want more than one bars in the chart?
write multiple plt.bar command, make sure they have different colors.
If multiple coordinates of different things are same (aka X coordinates) than the last color will be visible

experiment (Label changing on the Axis)
1. xticks for changing x axis labels, yticks for changing y axis labels.
2. first param is the list of locations on the axis, second is the list of the labels of those locations.

'''

##plt.bar(x, y, label='Just checking', color='g')
##plt.bar(x2, y2, label='Done checking', color='b')
##plt.xticks(x, alpha, rotation='vertical')
##plt.yticks(y, beta)
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.title("Good plot, just look at it!!")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.show()
