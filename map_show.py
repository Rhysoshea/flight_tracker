import urllib.request
import json
import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM


#define figure
fig, ax = plt.subplots()

#set axis for plotting area
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_ylim(40.6051, 40.6825)
ax.set_xlim(-73.8288,-73.7258)

#add osm basemap
osm_tiles=OSM()
ax.add_image(osm_tiles,13)#zoom level 13

#plot jfk intl airport
ax.text(-73.778889, 40.639722,'JFK Intl', horizontalalignment='right',size='large')
ax.plot([-73.778889],[40.639722],'bo')#plot blue point

plt.show()