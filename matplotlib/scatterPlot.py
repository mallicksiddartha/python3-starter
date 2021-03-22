from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
font_dict = {'family':'serif',
                 'color':'darkred',
                 'size':15}

plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")
plt.text(x[5], y[5], 'pong pong', fontdict=font_dict)

bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    
plt.annotate(str(y[-1]), (x[-1], y[-1]),
                 xytext = (x[-1]+0.5, y[-1]), bbox=bbox_props)
##plt.annotate('ano ano',
##             xy=(x[2], y[2]),
##             xytext=(0.8, 0.9),
##             textcoords='axes fraction',
##             arrowprops=dict(facecolor='black', shrink=0.05))

plt.title("Gunjaman Smokadallthetime")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.show()
