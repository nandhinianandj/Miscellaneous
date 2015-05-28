import timeit
s = """\
try:
    str.__nonzero__
except AttributeError:
    pass
"""

print timeit.timeit(stmt=s, number=100000)
