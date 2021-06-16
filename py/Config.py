import ee
import os
import time

ts = time.time()
timestamp = int(ts)           


### VARIABLES TO BE MODIFIED ####
### <--- FROM HERE ---> ###

USER_NAME = 'rohit'           # NAME OF OPERATOR USING THE CODE, OUTPUTS ARE STORED IN FOLDER WITH THEIR NAME
gtpt_asset = ee.FeatureCollection('users/rhtkhati/gt-pt-2019-2021-120m')           # Feature collection used as label data
spatial_resolution = 120           # resolution of output image
epochs = 50           # number of total pass of the training dataset
lr_rate = 0.0001           # learning rate
batch_size = 100           # total number of points in one batch


base_distance = 5000           ## only to be increased IF extent of output lc_map is smaller than extent of AOI


### DEFINE THE NAME, EXTENT OF REGION OF INTEREST WITH INTERESTED YEAR
ROI = {
    'cityName': 'Chittagong',
    'LatMax': 22.4525957509930443,
    'LatMin': 22.1544461679352587,
    'LonMax': 91.9732519334708627,
    'LonMin': 91.7009214895644647,
    'yearBegin':2020,
    'yearEnd':2020,
    'doyFilter':ee.Filter.And(ee.Filter.greaterThanOrEquals('doy',  1), ee.Filter.lessThanOrEquals('doy',  366)),
    'doyFilterLandsat': ee.Filter.dayOfYear(1,366)
}

### <--- TILL HERE ----> ####



city_name = ROI['cityName']
year_begin = ROI['yearBegin']
year_end = ROI['yearEnd']

IMAGE_FILE_PREFIX = city_name + '_' + str(year_begin) + '_' + str(year_end)
FOLDER_NAME = USER_NAME + '_' + IMAGE_FILE_PREFIX + '_' + str(timestamp)

kernel_radius = 1
kernel = ee.Kernel.gaussian(kernel_radius)
distance = 370000
cloud = 30

patch_size = 256
buffer_distance = base_distance * (round((spatial_resolution * 0.5 * patch_size)/base_distance) +1)           # extended region to include whole region of aoi

N_CLASSES = 4           # total number of features to be classified
LABEL = 'class'         # property name corresponding to feature [0, N_CLASSES)


### GOOGLE CLOUD STORAGE PATH REALTED VARIABLES
OUTPUT_BUCKET      = 'lc-mapping'
file_extension     = '.tfrecord.gz'
BUCKET_PATH        = 'gs://' + OUTPUT_BUCKET
USER_PATH          = USER_NAME + '/' + FOLDER_NAME
    
TRAIN_FILE_PREFIX  = USER_PATH + '/' +'datasets/Training_' + str(timestamp)
TEST_FILE_PREFIX   = USER_PATH + '/' +'datasets/Testing_' + str(timestamp)
INPUT_IMAGE_PREFIX = USER_PATH + '/inputs/' + IMAGE_FILE_PREFIX
FCC_IMAGE_PREFIX   = USER_PATH + '/outputs/' + IMAGE_FILE_PREFIX + '_fcc'

TRAIN_FILE_PATH    = BUCKET_PATH + '/' + TRAIN_FILE_PREFIX + file_extension
TEST_FILE_PATH     = BUCKET_PATH + '/' + TEST_FILE_PREFIX + file_extension
INPUT_FILE_PATH    = BUCKET_PATH + '/' + USER_PATH + '/inputs/'

OUTPUT_IMAGE_TFR   = BUCKET_PATH + '/' + USER_PATH + '/outputs/'+ IMAGE_FILE_PREFIX+'.TFRecord'


### REMOTE COMPUTER PATHS FOR REMOTE COMPUTER
OUTPUT_DIR         = './' + USER_PATH
JSON_PATH          = OUTPUT_DIR + '/json'
MODEL_PATH         = USER_PATH + '/model'
LC_DIR             = OUTPUT_DIR + '/lc-map/'
FC_DIR             = OUTPUT_DIR + '/fc-map/'
LC_IMAGE_TIF       = LC_DIR + IMAGE_FILE_PREFIX+'.tif'


### CREATES DIRECTORY IF NOT EXISTS
os.makedirs(MODEL_PATH, exist_ok = True)
os.makedirs(JSON_PATH, exist_ok = True)
os.makedirs(LC_DIR, exist_ok = True)
os.makedirs(FC_DIR, exist_ok = True)