# wrf-python development environment

A dockerized development environment for WRF-PYTHON

Contains:
---
netCDF4 
matplotlib 
cartopy
cython
wrf-python 


```bash
git clone https://github.com/tecfu/wrf-python-dev-env
```

## Running

### wrf-python

Drops you into a container where wrf-python is installed.

```bash
docker-compose -f ./wrf-python/docker-compose.yml run --rm wrf-python
```

You can then run wrf-python scripts via:

```bash
python /path/to/script.py
```

---

### ncdump-json
A \*.nc file dumper

```bash
docker-compose -f ./wrf-python/docker-compose.yml run --rm ncdump-json /path/to/file.nc
```

----

### netcdf4
A \*.nc file dumper
*Note that netcdf4 is compatible with node 8 only*

```bash
docker-compose -f ./wrf-python/docker-compose.yml run --rm  netcdf4
```


## Notes

- https://www.pkrc.net/wrf-lambert.html


### License

GPL 2.0
