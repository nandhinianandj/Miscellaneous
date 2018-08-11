import itertools
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-2) + fib(n-1)


def even_fibs(n):
    res = list()
    while n > 0:
        num = fib(n)
        if num %2 == 0:
            res.append(num)
        n = n-1
    print(res)
    return res

MAX_VAL = 4000000
#MAX_VAL = 4
ans=0
x = 1
fib_num = fib(x)
while fib_num < MAX_VAL:
    if fib_num % 2 ==0:
        print(fib_num)
        ans += fib_num
    x += 1
    fib_num = fib(x)

print(ans)

