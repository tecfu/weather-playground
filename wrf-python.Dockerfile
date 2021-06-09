FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
RUN apt update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:jonathonf/vim
RUN add-apt-repository ppa:ubuntugis/ppa
RUN apt update

RUN apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata


RUN apt install -y git python3-pip gfortran libgeos++-dev libproj-dev proj-data proj-bin libgeos-dev curl vim gdal-bin libgdal-dev python3-setuptools cdo netcdf-bin 
#RUN apt install python-pyproj
WORKDIR /root
RUN git clone --recurse-submodules git://github.com/tecfu/.vim
RUN sh -c .vim/INSTALL.sh
RUN git clone https://github.com/tecfu/.terminal
RUN /bin/bash .terminal/INSTALL.sh
WORKDIR /home
RUN git clone https://github.com/NCAR/wrf-python
WORKDIR wrf-python/
RUN pip3 install netCDF4 
RUN pip3 install matplotlib 
RUN pip3 install cartopy 
RUN pip3 install cython
RUN pip3 install wrf-python

#RUN pip3 install pyproj joblib cftime
WORKDIR /home
RUN pip3 download GDAL==2.4.2
RUN tar -xvzf GDAL-2.4.2.tar.gz
WORKDIR GDAL-2.4.2
RUN python3 setup.py build_ext --include-dirs=/usr/include/gdal/
RUN python3 setup.py install
RUN pip3 install .
WORKDIR /home/mnt
