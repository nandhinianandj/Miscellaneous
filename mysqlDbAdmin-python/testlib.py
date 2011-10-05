from random import seed
from time import time
import sys


sys.path.append('../v170/cgi-bin')
random_seed = int(time())



sizes = ['small','medium','large']

test_db  = 'emotionML'
#Change these settings before running the test suite.
use_size = 'small'

## Selenium variables
base_url = "http://127.0.0.1"
