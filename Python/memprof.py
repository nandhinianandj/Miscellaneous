from memory_profiler import profile
from memory_profiler import memory_usage

#@profile(precision=4)
def my_func(n):
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


memory_usage((my_func, (1,), ))

 # define a simple function
def f(a, n=100):
    import time
    time.sleep(2)
    b = [a] * n
    time.sleep(1)
    return b

from memory_profiler import memory_usage
memory_usage((f, (1,), {'n' : int(1e6)}))
