import urllib.request
import json
from matplotlib.path import Path

import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM


##ax = plt.axes(projection=ccrs.Mollweide())
##ax.stock_img()
##plt.show()

#define figure
##fig, ax = plt.subplots()



#add osm basemap

osm_tiles=OSM()
ax = plt.axes(projection=osm_tiles.crs)
ax.set_extent((-73.76, -73.80, 40.63, 40.65))
#set axis for plotting area
##ax.set_ylim(40.6051, 40.6825)
##ax.set_xlim(-73.8288,-73.7258)

ax.add_image(osm_tiles,15)#zoom level 13

#plot jfk intl airport
ax.text(-73.778889, 40.639722,'JFK Intl', horizontalalignment='right',size='large')
ax.plot([-73.778889],[40.639722],'bo')#plot blue point

plt.show()

