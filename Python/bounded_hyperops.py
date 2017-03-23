from hyperop import bounded_hyperop
Hb = bounded_hyperop(4, bound=1000)
print Hb(2,3), Hb(2,4)
