import cartopy
import cartopy.crs as ccrs
import salem
import pyproj

ds = salem.open_wrf_dataset('./o3_15-05-19_10.nc')
ds.HGT_M.where(ds.LANDMASK).salem.quick_map(cmap='topo');

# Define the projection
globe = ccrs.Globe(ellipse='sphere', semimajor_axis=6370000, semiminor_axis=6370000)
lcc = ccrs.LambertConformal(globe=globe, # important!
                            central_longitude=ds.STAND_LON, central_latitude=ds.MOAD_CEN_LAT,
                            standard_parallels=(ds.TRUELAT1, ds.TRUELAT2),
                            )
ax = plt.axes(projection=lcc)
z.plot(ax=ax, transform=lcc, cmap='terrain');
ax.coastlines()
ax.add_feature(cartopy.feature.BORDERS, linestyle='-');
ax.set_extent([xx.min(), xx.max(), yy.min(), yy.max()], crs=lcc)
