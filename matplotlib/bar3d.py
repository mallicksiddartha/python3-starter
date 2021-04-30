from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')


##x = np.array([[1,2,3,4,5,6,7,8,9,10]])
##y = np.array([[5,6,7,8,2,5,6,3,7,2]])
##z = np.array([[1,2,6,3,2,7,3,3,7,2]])

## x, y, z is the co-ordinates of the bars
## dx, dy, dz is depth of the bars in x axis, y axis, z axis accordingly.

x = [1,8,12]
y = [5,6,7]
z = [1,2,6]
dx = [2,1,3]
dy = [4,2,1]
dz = [3,4,5]

ax1.bar3d(x,y,z,dx,dy,dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')


plt.show()
