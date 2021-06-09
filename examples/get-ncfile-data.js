var netcdf4 = require("netcdf4");
var file = new netcdf4.File(`${__dirname}/o3_15-05-19_10.nc`, "r");
debugger
var target = file['root']['variables']['o3']['attributes']['projection']
var output = JSON.stringify(target, null, 2)
console.log(output)
