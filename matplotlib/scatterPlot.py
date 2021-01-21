from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")

plt.title("Gunjaman Smokada Allthetime")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.show()
