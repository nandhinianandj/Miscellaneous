# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name :
#
#* Purpose :
#
#* Creation Date : 25-08-2025
#
#* Last Modified : Monday 25 August 2025 09:39:50 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#
from pprint import pprint as pp
import matplotlib.pyplot as plt
from numpy.random import random, choice

x, y = random(), random()
for _ in range(100000):
    x, y = (-x + y)/2, (-x - y)/2
    x -= choice([0, 1])
    plt.plot(x, y, 'bo', markersize=1)
plt.show()

