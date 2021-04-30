from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map1 = Basemap(projection='mill',
            llcrnrlat = 20,
            llcrnrlon = 85,
            urcrnrlat = 30,
            urcrnrlon = 95,
            resolution='h')

map1.drawcoastlines()
map1.drawcountries()
##map1.drawstates(color='b')
##map1.etopo()

DHlat, DHlon = 23.8103, 90.4125
xs = []
ys = []

xpt, ypt = map1(DHlon, DHlat)

xs.append(xpt)
ys.append(ypt)
SYLlon, SYLlat = 91.8687, 24.8949

xpt, ypt = map1(SYLlon, SYLlat)
xs.append(xpt)
ys.append(ypt)

map1.plot(xs[0], ys[0], 'c*', markersize=15)
map1.plot(xs[1], ys[1], 'g^', markersize=15)

map1.plot(xs, ys, color='r', linewidth=3, label='Flight DTS001')
map1.drawgreatcircle(DHlon, DHlat, SYLlon, SYLlat, del_s=10.0, color='aquamarine', linewidth=3, label='Arc')

plt.legend(loc=4)
plt.title('Basemap Intro')
plt.show()
