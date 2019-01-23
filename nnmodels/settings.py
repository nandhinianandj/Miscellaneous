import pathlib

import numpy as np
import os

LABELS = ("kidney_stone",)
MODELS_BASE_PATH = os.environ.get('MODELS_BASE_PATH', './data/models')
MODEL_PERF_TRACKER = os.environ.get(
    'MODEL_PERF_TRACKER', './data/models/models_performance.csv')
MODEL_PERF_FIELDS = ['timestamp', 'modelname', 'modelfile',
                     'validation_loss', 'validation_accuracy',
                     'batch_size', 'epochs']


class ImageCropSettings(object):
    """
    Configuration object that holds the original
    - INPUT_SIZE for input image,
    - points for cropping (TOP_LEFT, BOTTOM_RIGHT)
    - IMAGE_SIZE image size used by the network
    """
    TOP_LEFT = (630, 18)
    BOTTOM_RIGHT = (996+630, 18+1044)
    INPUT_SIZE = (1920, 1080)
    IMAGE_SIZE = (416, 416)


class YoloModelSettings(ImageCropSettings):
    """test configuration for Yolo Model"""
    GRID_SIZE = (13, 13)
    BOX = 5
    CLASS = len(LABELS)
    CLASS_WEIGHTS = np.ones(CLASS, dtype='float32')

    # Anchors are pairs of x,y coordinates in 1 dimensional list ;)
    # These are 5 "anchors" (actually width/height ratios of objects)
    # In yolov2, these are at the last layer. To get Pixel Coordinates multiply
    # by 32
    ANCHORS = [0.57273, 0.677385, 1.87446, 2.06253, 3.33843,
               5.47434, 7.88282, 3.52778, 9.77052, 9.16828]

    NO_OBJECT_SCALE = 1.0
    OBJECT_SCALE = 5.0
    COORD_SCALE = 1.0
    CLASS_SCALE = 1.0

    BATCH_SIZE = 32
    WARM_UP_BATCHES = 0
    TRUE_BOX_BUFFER = 50
import os

INPUT_DIR='./data/texture_samples'
MODELS_BASE_PATH='./models'
PLOTS_DIR='./plots'
STANDARD_IMAGES_DIR='./data/standard_images'

CLASSES = ['porous', 'fibrous', 'crystalline']#, 'blotchy']
NUM_CLASSES = len(CLASSES)

IMAGE_SIZE=(400, 300)
MODEL_PERF_TRACKER='models_comparison.csv'
TEST_DATASET_FRAC=0.2
## Model types
POSSIBLE_MODELS = ['keras-cnn', 'keras-inception']

## Input tyes
POSSIBLE_INPUTS=['color-raw-images', 'gray-raw-images',
                 'color-gabor-filtered', 'gray-gabor-filtered',
                 'gray-wavelet-coeffs']

## Optimizer types
POSSIBLE_OPTIMIZERS=['adagrad', 'adadelta', 'sgd', 'rmsprop', 'adam']

## NN model settings
BATCH_SIZE=18
EPOCHS=100
AUGMENTED_SAMPLE_SZ = 5000
# FEATURE filter settings
GABOR_KSIZE=39
WAVLET='bior2.2'
WAVLET_LVL=None  #Use None for default max values
