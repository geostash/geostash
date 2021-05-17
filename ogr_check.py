from osgeo import ogr

driver_name_list = [ogr.GetDriver(id).GetName() for id in range(ogr.GetDriverCount())]
for driver_name in sorted(driver_name_list):
    ds = ogr.GetDriverByName(driver_name)
    if ds is not None:
        print(driver_name)
