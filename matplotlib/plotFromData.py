import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

## open file with csv module
##with open('exampleFile.csv','r') as csvfile:
##    plots = csv.reader(csvfile, delimiter=',')
##    for row in plots:
##        x.append(int(row[0]))
##        y.append(int(row[1]))

## open file using numpy
x,y = np.loadtxt('exampleFile.csv', delimiter=',', unpack=True)

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
