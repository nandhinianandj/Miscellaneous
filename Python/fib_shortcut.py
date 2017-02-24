def fib(n):
    #Short formula for approximating fibonacci no.
    return [int(round(((1+sqrt(5))**n - (1-sqrt(5))**n)/(2**n*sqrt(5)))) for n in range(128)]
