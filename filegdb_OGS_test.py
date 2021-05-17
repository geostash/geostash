   
import gdal
import ogr
from gdalconst import *

shp = "C:\\Data\\Projects_GIS\\2020\\001_a_GEODB\\BRK_Mapping_Pluvial_IT_US\\pluvial_brk_302.shp"
driver = ogr.GetDriverByName('ESRI Shapefile')

dataset = driver.Open(shp)    
layer = dataset.GetLayer()
layer.GetFeatureCount()    
schema = layer.schema
fields = [field.GetName() for field in schema]    
feature = layer.GetNextFeature()

from osgeo import ogr
driver = ogr.GetDriverByName("OpenFileGDB")
ds = driver.Open("C:\\Data\\Projects_GIS\\2020\\001_a_GEODB\\BRK_Mapping_Pluvial_IT_US\\BRK_input.gdb", 0)
print(ds)
b = ds.GetLayer("buildings")
sr = b.GetSpatialRef()
print(sr)

## Gdaltools

##import gdaltools
##
##import gdaltools
##info = gdaltools.gdalinfo("/mypath/myraster.tif")
##print info # output is the same generated by the gdalinfo command
##
##stats = gdaltools.get_raster_stats("/mypath/myraster.tif")
##print stats[0]
### outputs a tuple: (band0_min, band0_max, band0_mean, band0_stdev)
##print stats[1]
### outputs a tuple: (band1_min, band1_max, band1_mean, band1_stdev)
##
### Basic usage:
##info = gdaltools.ogrinfo("thelayer.shp", "thelayer", geom=False)
##print info # output is the same generated by the ogrinfo command
##
### Other examples:
##ogrinfo("thedb.sqlite")
##gdaltools.ogrinfo("thedb.sqlite", "layer1", "layer2", geom="SUMMARY")
##gdaltools.ogrinfo("thedb.sqlite", sql="SELECT UpdateLayerStatistics()")

##layer = shp
##
##ogr = gdaltools.ogr2ogr()
##ogr.set_encoding("UTF-8")
##ogr.set_input(layer, srs="EPSG:4326")
##ogr.set_output('layer.geojson')
##ogr.execute()

##Get detailed info for FileGDB:
##ogrinfo -al "C:\somefolder\MyGDB.gdb"
##Get detailed info for a zipped FileGDB:
##ogrinfo -al "C:\somefolder\MyGDB.gdb.zip"

import os, subprocess

##base_path = "some/file/path"
##loadfile = os.path.join(base_path, "file.xml")
##
##command = "C:\\Program Files\\QGIS Chugiak\\bin\\ogr2ogr.exe --config  PG_LIST_ALL_TABLES YES -f \"PostgreSQL\" -append PG:\"host=hostname user=username password=password dbname=dbname\" " + loadfile
##dcommand in subporocess
##command = ["C:\\ProgramData\\Anaconda3-2020.02\\envs\\Azureproc\\Library\\bin\\ogr2ogr.exe", 
##          "--config", "PG_LIST_ALL_TABLES", "YES", "-f", "PostgreSQL", "-append",
##          "PG:\"host=hostname user=username password=password dbname=dbname\"",
##           loadfile]

#### working
##command= ["C:\\ProgramData\\Anaconda3-2020.02\\envs\\Azureproc\\Library\\bin\\ogrinfo.exe", "-al", shp]
##subprocess.check_call(command)

####working
##command= "C:\\ProgramData\\Anaconda3-2020.02\\envs\\Azureproc\\Library\\bin\\ogrinfo.exe -al %s"% (shp)
##os.system(command)

##Read layer from FileGDB and load into PostGIS:
##ogr2ogr -overwrite -f "PostgreSQL" PG:"host=myhost user=myuser dbname=mydb password=mypass" "C:\somefolder\BigFileGDB.gdb" "MyFeatureClass"

##It can also be chained in a single line:
##
##gdaltools.ogr2ogr()\
##  .set_encoding("UTF-8")\
##  .set_input("mylayer.shp", srs="EPSG:4326")\
##  .set_output("mylayer.geojson").execute()
##
##
####Ogr2ogr. From postgis to shp:
##
##ogr = gdaltools.ogr2ogr()
##conn = gdaltools.PgConnectionString(host="localhost", port=5432, dbname="scolab", schema="data", user="myuser", password="mypass")
##ogr.set_input(conn, table_name="roads", srs="EPSG:4326")
##ogr.set_output("mylayer.shp")
##ogr.execute()
##
##Ogr2ogr. From postgis to spatialite, specifying a different output table name:
##
##ogr = gdaltools.ogr2ogr()
##conn = gdaltools.PgConnectionString(host="localhost", port=5432, dbname="scolab", schema="data", user="myuser", password="mypass")
##ogr.set_input(conn, table_name="roads", srs="EPSG:4326")
##ogr.set_output("mydb.sqlite", table_name="roads2010")
##ogr.set_output_mode(data_source_mode=ogr.MODE_DS_CREATE_OR_UPDATE) # required to add the layer to an existing DB
##ogr.execute()
##
##Ogr2ogr. From postgis to spatialite, reprojecting to "EPSG:25830":
##
##ogr = gdaltools.ogr2ogr()
##conn = gdaltools.PgConnectionString(host="localhost", port=5432, dbname="scolab", schema="data", user="myuser", password="mypass")
##ogr.set_input(conn, table_name="roads", srs="EPSG:4326")
##ogr.set_output("mydb.sqlite", srs="EPSG:25830")
##ogr.execute()



####Uploading Shapefile to postgres:
##
##import os
##connection = r"host=localhost port=5432 dbname=db1 user=postgres password=password"
##schema = "schemaname"
##target_shp = r"D:\Data\shapefile.shp"
##command = r'start cmd /K ogr2ogr -f "PostgreSQL" PG:"%s" -lco SCHEMA=%s "%s" -overwrite -progress -lco OVERWRITE=YES' % (connection, schema, target_shp)
##print(command)
##os.system(command,)
##
####Uploading an ESRI FileGeodatabase Feature class to postgres:
##import os
##connection = r"host=localhost port=5432 dbname=db1 user=postgres password=password"
##schema = "schemaname"
##target_gdb = r"D:\Data\Geodatabase.gdb"
##target_fc = "FeatureClassName"
##command = r'start cmd /K ogr2ogr -f "PostgreSQL" PG:"%s" -lco SCHEMA=%s "%s" "%s" -overwrite -progress -lco OVERWRITE=YES' % (connection, schema, target_gdb, target_fc)
##print(command)
##os.system(command,)
##If you want to upload the entire GeoDatabase, not just a Feature Class, then remove the last "%s" in the 'command' variable and remove the 'target_fc' line. Also remove the reference to 'target_fc' at the end of the 'command' variable.



##import subprocess

##subprocess.run(r'ogr2ogr -lco PRECISION=NO -lco SRID=27700 -lco SPATIAL_INDEX=NO -lco OVERWRITE=YES -lco UPLOAD_GEOM_FORMAT=wkt -f "MSSQLSpatial" "MSSQL:server=server;database=db;trusted_connection=yes" PG:"dbname=db host=host port=1234 user=user password=pass" "schema.table" -t_srs "EPSG:27700" -s_srs "EPSG:27700" -a_srs "EPSG:27700" -gt 100000 -progress -nln schema.table', check=True, shell=True)
##import subprocess
##
##subprocess.run(r'pgsql2shp -f "output_shapefile.shp" -h host -u postgres_user -P postgres_password database_name schema.export_table', check=True, shell=True)