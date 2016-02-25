
from hyperop import hyperop
import mpmath
def GrahamsNumber():
    # This may take awhile...
    g = 4
    for n in range(1,64+1):
        g = hyperop(g+2)(3,3)
    return g

# Phase angle on complex plane
H = hyperop(4)
f = lambda z: H(z,4)
mpmath.cplot(f, verbose=True, points=100000)

# Bounded HyperOps
from hyperop import bounded_hyperop
Hb = bounded_hyperop(4, bound=1000)
print Hb(2,3), Hb(2,4)
# >> 16 inf
