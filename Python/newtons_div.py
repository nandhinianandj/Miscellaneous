from mpmath.libmp.libintmath import giant_steps,lshift,rshift
from math import log

import timeit

START_PREC = 15

def size(x):
    if isinstance(x, (int, long)):
        return int(log(x,2))
    # GMPY support
    return x.numdigits(2)

def newdiv(p, q):
    szp = size(p)
    szq = size(q)
    szr = szp - szq
    if min(szp, szq, szr) < 2*START_PREC:
        return p//q

    #import pdb;pdb.set_trace()
    r = (1 << (2*START_PREC)) // (q >> (szq - START_PREC))
    last_prec = START_PREC
    for prec in giant_steps(START_PREC, szr):
        a = lshift(r, prec-last_prec+1)
        b = rshift(r**2 * rshift(q, szq-prec), 2*last_prec)
        r = a - b
        last_prec = prec
    return ((p >> szq) * r) >> szr

def main():
    trial_runs = 30
    print "mpmath + newton's division method"
    print "timeit output %d times run"%trial_runs
    print timeit.timeit(stmt="newdiv(10244203,131)",setup="from __main__ import newdiv",number=trial_runs)
    print newdiv(10244203,131)
    pass
if __name__ == '__main__':
    main()
