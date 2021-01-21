from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
days = [1,2,3,4,5,6,7]

sleeping = [8,9,7,7,9,8,9]
working = [5,5,5,4,6,4,5]
exercising= [3,2,3,4,2,3,2]
eating = [4,4,4,4,4,5,4]
playing = [4,4,5,3,4,4,4]
'''
Need to add empty plot because stack plot doesn't allow labels.
'''
plt.plot([],[],label='Sleeping', color='r')
plt.plot([],[],label='Working', color='y')
plt.plot([],[],label='Exercising', color='purple')
plt.plot([],[],label='Eating', color='g')
plt.plot([],[],label='Playing', color='c')

plt.stackplot(days,sleeping,working,exercising,eating,playing, colors=['r','y','purple','g','c'])

plt.title("Gunjaman Smokada Allthetime")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.show()
