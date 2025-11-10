from geopandas import read_file

world = read_file("C:/Users/ROG/Desktop/understandinggis/data/natural-earth/ne_50m_admin_0_countries.shp")

print(world.head())