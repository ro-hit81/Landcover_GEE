import ee

service_account = 'glodal-landcover-mapping@rohit-81.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'glodal_gee.json')
ee.Initialize(credentials)

class Product:
    def __init__(self, ids, st_yr, ed_yr, d_ftr, ext, cl):
        self.landsat_id = ids
        self.start_year = st_yr
        self.end_year = ed_yr
        self.doy_filter = d_ftr
        self.extent = ext
        self.cloud = cl
        
    def cloudMask(img):
        return img.updateMask(img.select('BQA').lt(64))
        
    def select_product(self):
        
        if(self.landsat_id == 'LANDSAT/LM01/C01/T2' or self.landsat_id == 'LANDSAT/LM02/C01/T2' or self.landsat_id == 'LANDSAT/LM03/C01/T1'):
            image = ee.ImageCollection(self.landsat_id)
            image = image.filterDate(str(self.start_year) + '-01-01', str(self.end_year) + '-12-31')
            image = image.filter(self.doy_filter)
            image = image.filterBounds(self.extent).filterMetadata('CLOUD_COVER_LAND', 'less_than', 20)
            image = image.map(cloudMask).reduce(ee.Reducer.median())
            return {
                'region': image.geometry().bounds().getInfo(),
                'image': image,
                'image_int': image.toByte()       
            }
        else:
            image_col = ee.ImageCollection(self.landsat_id)
            image_col = image_col.filterDate(str(self.start_year) + '-01-01', str(self.end_year) + '-12-31')
            image_col = image_col.filter(self.doy_filter).filterBounds(self.extent)
            return {
                'region': image_col.geometry().bounds().getInfo(),
                'image': ee.Algorithms.Landsat.simpleComposite(image_col, 50, self.cloud, 40, True),
                'image_int': ee.Algorithms.Landsat.simpleComposite(image_col, 50, self.cloud, 40, False)
            }
        