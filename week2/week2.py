from geopandas import read_file, GeoSeries

# load the shapefile of countries - this gives a table of 12 columns and 246 rows (one per country)
world = read_file("C:/Users/ROG/Desktop/understandinggis/data/natural-earth/ne_10m_admin_0_countries.shp")

usa = world.loc[(world.ISO_A3 == 'USA')]

print(type(usa))

usa_col = usa.geometry

print(type(usa_col))

# extract the geometry objects themselves from the GeoSeries
usa_geom = usa_col.iloc[0]

print(type(usa_geom))