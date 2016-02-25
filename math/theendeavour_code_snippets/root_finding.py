#Assume a <b, fa = f(a) < 0, fb = f(b)>0
def noisy_bisect(f,a,b,fa,fb,tolerance):
    if b-a <tolerance:
        return (a,b)
    mid = 0.5*(a+b)
    fmid = f(mid)
    if fmid <fa or fmid >fb:
        #Monotonicity violated. Reached resolution of noise.
        return (a,b)
    if fmid <0:
        a,fa = mid, fmid
    else:
        b,fb = mid, fmid
    return noisy_bisect(f, a, b, fa, fb, tolerance)

from scipy.stats import norm
from time import sleep
noise = norm(0,0.01)

def f(x):
    sleep(10)
    return x**2 -1 + noise.rvs()


def f1(x,N):
    sleep(N)
    noise = norm(0,0.1/sqrt(N))
    return x**2 -1 + noise.rvs()
a=0
b=3
fa = f(a)
fb = f(b)
print noisy_bisect(f,a,b,fa,fb,0.0001)

