from math import sqrt
def fibonacci(n: Integer) -> [Integer]:
    l = []
    if len(l) < n :
        for i in range(n-len(l)):
            l.append(l[-1] +l[-2])
    return l

print(fibonacci(4))
