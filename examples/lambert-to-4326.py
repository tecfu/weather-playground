from netCDF4 import Dataset
from wrf import (LambertConformal)
from osgeo import osr

# https://unidata.github.io/python-training/workshop/Bonus/netcdf-writing/
ncfile = Dataset('./o3_15-05-19_10.nc', mode='r')
#print(ncfile)
#print(ncfile.variables.o3.attributes.projection) #fails because netCDF4 is fucking retarded
print(ncfile.variables['o3']) #fails because netCDF4 is fucking retarded

## hardcoding `lambert conformal conic` values because can't extract from ncfile
TRUELAT1 = 22.273000717163086
TRUELAT2 = 22.273000717163086
MOAD_CEN_LAT = 22.272972106933594
STAND_LON = 97.16400146484375
POLE_LAT = 90.0
POLE_LON = 0
#_LC = LambertConformal(TRUELAT1, TRUELAT2, MOAD_CEN_LAT, STAND_LON, POLE_LAT, POLE_LON)

_LC = LambertConformal(
    TRUELAT1=TRUELAT1,
    TRUELAT2=TRUELAT2,
    MOAD_CEN_LAT=MOAD_CEN_LAT,
    STAND_LON=STAND_LON,
    POLE_LAT=POLE_LAT,
    POLE_LON=POLE_LON
)

projection = _LC.proj4()
#print(projection)
#
#source = osr.SpatialReference()
#source.ImportFromEPSG(4326)
#target = osr.SpatialReference()
#target.ImportFromProj4(projection)
#transform = osr.CoordinateTransformation(source, target)
#print(transform)

# See: https://gis.stackexchange.com/a/8550/184010
srs = osr.SpatialReference()
# Imports PROJ4 to Spatial Reference Object
srs.ImportFromProj4(projection)
srs.MorphToESRI() # converts the PROJ4 to an ESRI-compatible format
print ("ESRI compatible PROJ4 for use as .prj:")
print (srs.ExportToProj4())


# Best example:
# https://gis.stackexchange.com/q/382458/184010
