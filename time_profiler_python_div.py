
from time import clock

def timing(INT):
    fmt = "%10s %12f %12f %12f %8s"
    print "%10s %12s %12s %12s %8s" % ("size", "old time", "new time",
        "faster", "error")
    print "-"*78
    for i in range(4,30):
        n = 2**i
        Q = INT(10)**n
        P = Q**2
        t1 = clock()
        R1 = P // Q
        t2 = clock()
        R2 = newdiv(P,Q)
        t3 = clock()
        size, old_time, new_time = n, t2-t1, t3-t2
        faster, error = old_time/new_time, R2-R1
        print fmt % (size, old_time, new_time, faster, error)
