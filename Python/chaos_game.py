# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name :
#
#* Purpose :
#
#* Creation Date : 25-08-2025
#
#* Last Modified : Monday 25 August 2025 09:41:50 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#
from pprint import pprint as pp
from scipy import sqrt, zeros
import matplotlib.pyplot as plt
from random import random, randint

def midpoint(p, q):
    return (0.5*(p[0] + q[0]), 0.5*(p[1] + q[1]))

# Three corners of an equilateral triangle
corner = [(0, 0), (0.5, sqrt(3)/2), (1, 0)]

N = 1000
x = zeros(N)
y = zeros(N)

x[0] = random()
y[0] = random()
for i in range(1, N):
    k = randint(0, 2) # random triangle vertex
    x[i], y[i] = midpoint( corner[k], (x[i-1], y[i-1]) )
    
plt.scatter(x, y)
plt.show()

