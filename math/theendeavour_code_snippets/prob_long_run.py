from math import log,exp

def prob(a, b, n, p):
    r = -log(n*(1-p))/log(p)
    cdf = lambda x: exp(- p**x )
    return cdf(b + 1 - r) - cdf(a - r)
