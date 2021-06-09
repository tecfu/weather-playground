# pip install salem pyproj netCDF4 shapely descartes
from netCDF4 import Dataset
from wrf import (to_np, getvar, smooth2d, get_cartopy, cartopy_xlim,
                 cartopy_ylim, latlon_coords, LambertConformal)
# import pyproj

## salem doesn't like the dataset
#import salem
#ds = salem.open_wrf_dataset('o3_15-05-19_10.nc')
#proj = 'lcc' # projection type: Lambert Conformal Conic
#lat_1 = ds.TRUELAT1
#lat_2 = ds.TRUELAT2 # Cone intersects with the sphere
#lat_0 = ds.MOAD_CEN_LAT
#lon_0 = ds.STAND_LON # Center point

## fucking useless data format doeesn't traverse
#ds = Dataset("o3_15-05-19_10.nc")
#print(ds['o3']['projection;'])

#wrf_proj = pyproj.Proj(proj, lat_1, lat_0, a=6370000, b=6370000)

## hardcoding the values...
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

_PRJ4 = _LC.proj4()
print(_PRJ4)


