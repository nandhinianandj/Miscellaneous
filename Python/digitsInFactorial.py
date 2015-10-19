from scipy.special import gammaln
from math import log, floor, pi

def digits_in_factorial(n):
    return floor( gammaln(n+1)/log(10.0) ) + 1

def stirling(n):
    return floor( ((n+0.5)*log(n) - n + 0.5*log(2*pi))/log(10) ) + 1

def digits_in_factorial(n, b=10):
    return floor( gammaln(n+1)/log(b) ) + 1

def stirling(n, b=10):
    return floor( ((n+0.5)*log(n) - n + 0.5*log(2*pi))/log(b) ) + 1
