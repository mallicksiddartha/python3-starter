from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
x = [1, 2, 5, 40]
y = [7, 6, 4, 2]
x2 = [1, 5, 7, 9]
y2 = [1, 8, 10, 16]

#plt.plot(x, y)
#plt.plot(x2, y2)
'''
Bar chart - You have x number of different things and you have their corresponding heights
the first list is the X coordinates of the different things, the second list is the height of those different
things.
You want more than one bars in the chart?
write multiple plt.bar command, make sure they have different colors.
If multiple coordinates of different things are same (aka X coordinates) than the last color will be visible

'''

plt.bar(x, y, label='Just checking', color='g')
plt.bar(x2, y2, label='Done checking', color='b')
plt.title("Good plot, just look at it!!")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.show()
