class Landsat:
    def __init__(self, target_year):
        self.year = target_year
        
    def select_landsat(self):
        
        if (self.year >= 2013):
            return {
                'bands': ['B2', 'B3', 'B4', 'B5', 'B6', 'B7'],
                'FCCbands': ['B5', 'B4', 'B3'],
                'TextureBand': ['B5'],
                'bandsClassify': ['B2', 'B3', 'B4', 'B5', 'B6', 'B7','B5_1'],
                'bandsGLCM': ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B5_asm', 'B5_contrast', "B5_corr", "B5_var", "B5_idm", "B5_savg", "B5_svar", "B5_sent", "B5_ent", "B5_dvar", "B5_dent", "B5_imcorr1", "B5_imcorr2","B5_maxcorr", "B5_diss",  "B5_inertia", "B5_shade", "B5_prom"],
                'Landsat': 'LANDSAT/LC08/C01/T1'
            }

        if (self.year >= 1999 and self.year <= 2002):
            return {
                'bands': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7'],
                'TextureBand': ['B4'],
                'bandsClassify': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7','B4_1'],
                'bandsGLCM': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'B4_asm', 'B4_contrast',"B4_corr", "B4_var","B4_idm","B4_savg", "B4_svar","B4_sent","B4_ent","B4_dvar","B4_dent","B4_imcorr1", "B4_imcorr2","B4_maxcorr","B4_diss","B4_inertia","B4_shade","B4_prom"],
                'FCCbands': ['B4', 'B3', 'B2'],
                'Landsat': 'LANDSAT/LE07/C01/T1'
            }

        if (self.year >= 1984 and self.year <= 1998 or self.year >=2003 and self.year <=2012):
            return{
                'bands': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7'],
                'bandsClassify': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7','B4_1'],
                'bandsGLCM': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'B4_asm', 'B4_contrast',"B4_corr", "B4_var","B4_idm","B4_savg", "B4_svar","B4_sent","B4_ent","B4_dvar","B4_dent","B4_imcorr1", "B4_imcorr2","B4_maxcorr","B4_diss","B4_inertia","B4_shade","B4_prom"],
                'FCCbands': ['B4', 'B3', 'B2'],
                'TextureBand': ['B4'],
                'Landsat': 'LANDSAT/LT05/C01/T1'
            }

        if (self.year == 1983):
            return{
                'bands': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7'],
                'bandsClassify': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7','B4_1'],
                'bandsGLCM': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'B4_asm', 'B4_contrast',"B4_corr", "B4_var","B4_idm","B4_savg", "B4_svar","B4_sent","B4_ent","B4_dvar","B4_dent","B4_imcorr1", "B4_imcorr2","B4_maxcorr","B4_diss","B4_inertia","B4_shade","B4_prom"],
                'FCCbands': ['B4', 'B3', 'B2'],
                'TextureBand': ['B4'],
                'Landsat': 'LANDSAT/LT04/C01/T1'
            }

        if (self.year >= 1979 and self.year <= 1982):
            return {
                'bands': ['B4_median', 'B5_median', 'B6_median','B7_median','B6_median_1'],
                'bandsClassify': ['B4_median', 'B5_median', 'B6_median', 'B7_median'],
                'FCCbands': ['B6_median', 'B5_median', 'B4_median'],
                'TextureBand': ['B6_median'],
                'Landsat': 'LANDSAT/LM03/C01/T1'
            }

        if (self.year >= 1975 and self.year <= 1978):
            return {
                'bands': ['B4_median', 'B5_median', 'B6_median','B7_median','B6_median_1'],
                'bandsClassify': ['B4_median', 'B5_median', 'B6_median', 'B7_median'],
                'FCCbands': ['B6_median', 'B5_median', 'B4_median'],
                'TextureBand': ['B6_median'],
                'Landsat': 'LANDSAT/LM02/C01/T2'
            }

        if (self.year >= 1972 and self.year <= 1974):
            return {
                'bands': ['B4_median', 'B5_median', 'B6_median','B7_median','B6_median_1'],
                'bandsClassify': ['B4_median', 'B5_median', 'B6_median', 'B7_median'],
                'FCCbands': ['B6_median', 'B5_median', 'B4_median'],
                'TextureBand': ['B6_median'],
                'Landsat': 'LANDSAT/LM01/C01/T2'
            }