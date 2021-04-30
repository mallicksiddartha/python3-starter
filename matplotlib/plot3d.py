from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

fig1 = plt.figure(1)
fig2 = plt.figure(2)
ax1 = fig1.add_subplot(111, projection='3d')

ax2 = fig2.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data() ## this creates n-dim lists for X,Y,Z
print(type(X))

A = np.array([[1,2,3,4],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4]])
B = np.array([[4,2,6, 5],
              [4,2,6, 5],
              [4,2,6, 5],
              [4,2,6, 5]])
C = np.array([[3,6,8, 7],
              [3,6,8, 7],
              [3,6,8, 7],
              [3,6,8, 7]])

x = np.array([[1,2,3,4,5,6,7,8,9,10]])
y = np.array([[5,6,7,8,2,5,6,3,7,2]])
z = np.array([[1,2,6,3,2,7,3,3,7,2]])
a = [1,2,3,4,5,6,7,8,9,10]
b = [4,4,1,7,3,8,1,6,3,7]
c = [7,8,4,9,9,4,8,6,3,9]

##ax1.plot(a, b, c)  ## This is a line graph in 3d plain, we see 1 line
ax1.scatter(a, b, c, c='g', marker='o')
ax1.scatter(x[0], y[0], z[0], c ='r', marker='o') ## The previous data remains, the new data is added
## to the graph

ax2.plot_wireframe(X,Y,Z, rstride = 5, cstride = 5)
##ax2.plot_wireframe(x, y, z) ## Needs list of lists as data type

##ax1.plot_trisurf(x, y, z)


ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

ax2.set_xlabel('x axis')
ax2.set_ylabel('y axis')
ax2.set_zlabel('z axis')

plt.show()
