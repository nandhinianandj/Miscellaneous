from math import sqrt
global l

def fib(num):
    #Short formula for approximating fibonacci no.
    return [int(round(((1+sqrt(5))**n - (1-sqrt(5))**n)/(2**n*sqrt(5)))) for n in range(num)]

def fibonacci(n):
    global l
    l = list([0,1])
    if len(l) < n :
        for i in range(n-len(l)):
            l.append(l[-1] +l[-2])


if __name__ == '__main__':
    print fibonacci(123)
    print l,len(l)
    a =fib(123)
    print a, len(a)
