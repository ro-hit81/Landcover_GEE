class Indices:
    def __init__(self, params, product):
        self.params = params
        self.product = product
        
    def add_indices(self):
        if(self.params['Landsat']=='LANDSAT/LC08/C01/T1'):
            swir  = self.product['image'].select('B6')
            nir   = self.product['image'].select('B5')
            red   = self.product['image'].select('B4')
            green = self.product['image'].select('B3')

            ndvi  = nir.subtract(red).divide(nir.add(red))
            ndbi  = swir.subtract(nir).divide(swir.add(nir))
            bi    = ndbi.subtract(ndvi)
            ndwi  = green.subtract(swir).divide(green.add(swir))

            self.product['image'] = self.product['image'].addBands([ndvi, ndbi, bi, ndwi])
            self.product['image'] = self.product['image'].rename('B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','ndvi','ndbi','bi','ndwi')

            self.params['bandsClassify'].extend(['ndvi', 'ndbi', 'bi', 'ndwi'])


        if(self.params['Landsat'] == 'LANDSAT/LE07/C01/T1'):
            swir  = self.product['image'].select('B5')
            nir   = self.product['image'].select('B4')
            red   = self.product['image'].select('B3')
            green = self.product['image'].select('B2')

            ndvi  = nir.subtract(red).divide(nir.add(red))
            ndbi  = swir.subtract(nir).divide(swir.add(nir))
            bi    = ndbi.subtract(ndvi)
            ndwi  = green.subtract(swir).divide(green.add(swir))

            self.product['image'] = self.product['image'].addBands([ndvi, ndbi, bi, ndwi])
            self.product['image'] = self.product['image'].rename('B1','B2','B3','B4','B5','B6_VCID_1','B6_VCID_2','B7','B8','ndvi','ndbi','bi','ndwi')

            self.params['bandsClassify'].extend(['ndvi', 'ndbi', 'bi', 'ndwi'])


        if(self.params['Landsat'] == 'LANDSAT/LM04/C01/T1' or self.params['Landsat'] == 'LANDSAT/LT05/C01/T1'):
            swir  = self.product['image'].select('B5')
            nir   = self.product['image'].select('B4')
            red   = self.product['image'].select('B3')
            green = self.product['image'].select('B2')

            ndvi  = nir.subtract(red).divide(nir.add(red))
            ndbi  = swir.subtract(nir).divide(swir.add(nir))
            bi    = ndbi.subtract(ndvi)
            ndwi  = green.subtract(swir).divide(green.add(swir))

            self.product['image'] = self.product['image'].addBands([ndvi, ndbi, bi, ndwi])
            self.product['image'] = self.product['image'].rename('B1','B2','B3','B4','B5','B6','B7','ndvi','ndbi','bi','ndwi')

            self.params['bandsClassify'].extend(['ndvi', 'ndbi', 'bi', 'ndwi'])


        if(self.params['Landsat'] == 'LANDSAT/LM01/C01/T2' or self.params['Landsat'] == 'LANDSAT/LM02/C01/T2' or self.params['Landsat'] == 'LANDSAT/LM03/C01/T1'):
            swir = self.product['image'].select('B6_median')
            nir = self.product['image'].select('B6_median')
            red = self.self.product['image'].select('B5_median')

            ndvi = nir.subtract(red).divide(nir.add(red))

            self.product['image'] = self.product['image'].addBands(ndvi)
            self.product['image'] = self.product['image'].rename('B4_median','B5_median','B6_median','B7_median','BQA_median','ndvi')

            self.params['bandsClassify'].append('ndvi')