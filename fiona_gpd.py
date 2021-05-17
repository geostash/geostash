import fiona 
import geopandas as gpd

gdb_file= "C:\\Data\\Projects_GIS\\2020\\001_a_GEODB\\BRK_Mapping_Pluvial_IT_US\\BRK_input.gdb"
# Get all the layers from the .gdb file 
layers = fiona.listlayers(gdb_file)

for layer in layers:
    gdf = gpd.read_file(gdb_file,layer=layer)
    # Do stuff with the gdf
