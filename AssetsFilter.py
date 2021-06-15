import ee

class Assets:
    def __init__(self, feat):
        self.feat = feat
        
    def reduce_class_value(self):
        return self.feat.set('class', ee.Number(self.feat.get('class')).subtract(1))