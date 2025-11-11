from geopandas import read_file, GeoSeries

# load the shapefile of countries - this gives a table of 12 columns and 246 rows (one per country)
world = read_file("C:/Users/ROG/Desktop/understandinggis/data/natural-earth/ne_10m_admin_0_countries.shp")

usa = world.loc[(world.ISO_A3 == 'USA')]
usa_col = usa.geometry
usa_geom = usa_col.iloc[0]

mex = world.loc[(world.ISO_A3 == 'MEX')]
mex_col = mex.geometry
mex_geom = mex_col.iloc[0]

# calculate the intersection of the geometry objects
border = usa_geom.intersection(mex_geom)

from matplotlib.pyplot import subplots, savefig, title
# create map axis object
my_fig, my_ax = subplots(1, 1, figsize=(16, 10))

# remove axes
my_ax.axis('off')

# plot the border
GeoSeries(border).plot(
  ax = my_ax
	)

# save the image
savefig('./out/first-border.png')

from pyproj import Geod
# set which ellipsoid you would like to use
geod = Geod(ellps='WGS84')

print(border)

# loop through each segment in the line and print the coordinates
    
# initialise a variable to hold the cumulative length
cumulative_length = 0

# loop through each segment in the line
for segment in border.geoms:
    print(f"from:{segment.coords[0]}\tto:{segment.coords[1]}")

	# THIS LINE NEEDS COMPLETING
    #distance = geod.inv(segment.coords[:-1], segment.coords[:-1], segment.coords[1:], segment.coords[1:])[2]
    distance = geod.inv(segment.coords[0][0], segment.coords[0][1], segment.coords[1][0], segment.coords[1][1])[2]

	# add the distance to our cumulative total
    cumulative_length += distance
 
    
lambert_conic="+proj=lcc +lon_0=-96.1523438 +lat_1=4.0847623 +lat_2=37.2835843 +lat_0=20.6841733 +datum=WGS84 +units=m +no_defs"
# open the graticule dataset
graticule = read_file("C:/Users/ROG/Desktop/understandinggis/data/natural-earth/ne_110m_graticules_5.shp")
# create map axis object
my_fig, my_ax = subplots(1, 1, figsize=(16, 10))

# remove axes
my_ax.axis('off')

# set title
title(f"Trump's wall would have been {cumulative_length / 1000:.2f} km long.")

# project border
border_series = GeoSeries(border, crs=world.crs).to_crs(lambert_conic)

# extract the bounds from the (projected) GeoSeries Object
minx, miny, maxx, maxy = border_series.geometry.iloc[0].bounds

# set bounds (10000m buffer around the border itself, to give us some context)
buffer = 10000
my_ax.set_xlim([minx - buffer, maxx + buffer])
my_ax.set_ylim([miny - buffer, maxy + buffer])

# plot data
usa.to_crs(lambert_conic).plot(
    ax = my_ax,
    color = '#ccebc5',
    edgecolor = '#4daf4a',
    linewidth = 0.5,
    )
mex.to_crs(lambert_conic).plot(
    ax = my_ax,
    color = '#fed9a6',
    edgecolor = '#ff7f00',
    linewidth = 0.5,
    )
border_series.plot(     # note that this has already been projected above!
    ax = my_ax,
    color = '#984ea3',
    linewidth = 2,
    )
graticule.to_crs(lambert_conic).plot(
    ax=my_ax,
    color='grey',
    linewidth = 1,
    )

# save the result
savefig('out/2.png', bbox_inches='tight')
print("done!")