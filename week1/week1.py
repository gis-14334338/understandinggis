from geopandas import read_file

world = read_file("C:/Users/ROG/Desktop/understandinggis/data/natural-earth/ne_50m_admin_0_countries.shp")
graticule = read_file("C:/Users/ROG/Desktop/understandinggis/data/natural-earth/ne_110m_graticules_15.shp")
bbox = read_file("C:/Users/ROG/Desktop/understandinggis/data/natural-earth/ne_110m_wgs84_bounding_box.shp")

print(world.head())
from matplotlib.pyplot import subplots, savefig

ea_proj = "+proj=eqearth +lon_0=0 +datum=WGS84 +units=m +no_defs"

world = world.to_crs(ea_proj)
graticule = graticule.to_crs(ea_proj)
bbox = bbox.to_crs(ea_proj)

world['pop_density'] = world['POP_EST'] / (world.area / 1000000)


# create map axis object
my_fig, my_ax = subplots(1, 1, figsize=(16, 10))

# plot the countries onto ax
# add bounding box and graticule layers
bbox.plot(
    ax = my_ax,
    color = 'lightgray',
    linewidth = 0,
    )

# plot the graticule
graticule.plot(
    ax = my_ax,
    color = 'white',
    linewidth = 0.5,
    )

world.plot(
    ax=my_ax,
    column="pop_density",   
    cmap="OrRd",         
    scheme="quantiles",    
    edgecolor="gray",
    linewidth=0.3,
    legend=True,
    legend_kwds={
        "loc": "lower left",
        "title": "Population Density (people/km²)"
    }
)


my_ax.set(title="Population Density: <INSERT PROJECTION NAME HERE> Coordinate Reference System")
my_ax.axis('off')

# save the result
savefig('./out/1.png')
print("done!")

