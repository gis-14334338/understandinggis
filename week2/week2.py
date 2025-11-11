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