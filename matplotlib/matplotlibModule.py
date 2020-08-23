from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
#x = [5, 6, 8, 14]
#y = [7, 6, 4, 2]
#x2 = [3, 5, 7, 9]
#y2 = [1, 8, 5, 6]

#plt.plot(x, y)
#plt.plot(x2, y2)

x,y = np.loadtxt('exampleFile.csv',
                 unpack=True,
                 delimiter=',')
print(x,'\n',y)
plt.plot(x,y, label='Oh look! A label')

plt.title("Good plot, just look at it!!")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.show()
