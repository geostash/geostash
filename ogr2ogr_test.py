## from https://github.com/OSGeo/gdal/blob/master/gdal/swig/python/gdal-utils/osgeo_utils/samples

import ogr2ogr

shp = "C:\\Data\\Projects_GIS\\2020\\001_a_GEODB\\BRK_Mapping_Pluvial_IT_US\\pluvial_brk_302.shp"
out_gjson= "C:\\Temp\\dump\\output.geojson"

ogr2ogr.main([
  'ogr2ogr',
  '-f', 'GeoJSON', 'output.geojson' ,
  shp
])
