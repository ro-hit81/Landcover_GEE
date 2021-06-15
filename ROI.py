import ee

cityName = 'Chittagong'
LatMax = 22.4525957509930443
LatMin = 22.1544461679352587
LonMax = 91.9732519334708627
LonMin = 91.7009214895644647
yearBegin = 2020
yearEnd = 2020
doyFilter = ee.Filter.And(ee.Filter.greaterThanOrEquals('doy',  1), ee.Filter.lessThanOrEquals('doy',  366))
doyFilterLandsat = ee.Filter.dayOfYear(1,366)}