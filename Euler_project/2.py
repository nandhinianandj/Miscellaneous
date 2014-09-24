import itertools

lines = list()
lines=[2,34,4]
#for line in fileinput.input():
#    lines.append(int(line))

def fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [2]
    else:
        print(fib(n-2), fib(n-1), n)
        return fib(n-2).append(fib(n-1))


def even_fibs(n):
    res = list()
    print(fib(n))
    for num in fib(n):
        if num %2 == 0:
            res.append(num)
    return res

for num in lines[1:]:
    print(sum([x*1 for x in even_fibs(num)]))

