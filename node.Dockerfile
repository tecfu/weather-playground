FROM node:8.16.0-alpine
RUN apk update && apk upgrade
RUN apk add --no-cache bash git vim python make
RUN git clone https://github.com/tecfu/wrf-python
WORKDIR wrf-python
RUN npm install netcdf4
