from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
## slice and activities are two independent list, try to make them a list of key value pair, then
## extract the list of values and the list of keys
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

sliceActivityPair = {'sleeping':7,'eating':2,'working':2,'playing':13}
plt.pie(sliceActivityPair.values(),
        labels=sliceActivityPair.keys(),
        colors=cols,
        startangle=90,
        shadow= True,
        counterclock=False,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()
