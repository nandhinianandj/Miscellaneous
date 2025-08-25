# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name :
#
#* Purpose :
#
#* Creation Date : 25-08-2025
#
#* Last Modified : Monday 25 August 2025 09:36:50 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#
from pprint import pprint as pp
import numpy as np
import matplotlib.pyplot as plt

A = np.linalg.inv(np.array([[2,  -1], [1, 2]]))
R = np.array([[2, -1, 0,  1, 1],
              [1,  2, 2,  2, 1]])

v = np.random.random(size=2)
for _ in range(100000):
    i = np.random.choice([0, 1, 2, 3, 4])
    v = np.dot(A, v) + R[:, i]
    plt.plot(v[0], v[1], 'bo', markersize=1)
plt.gca().set_aspect("equal")
plt.show()
