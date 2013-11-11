from math import sqrt
import timeit

l = list([0,1])

def fib(num):
    #Short formula for approximating fibonacci no.
    return [int(round(((1+sqrt(5))**n - (1-sqrt(5))**n)/(2**n*sqrt(5)))) for n in range(num)]

def fibonacci(n):
    global l
    if len(l) < n :
        for i in range(n-len(l)):
            l.append(l[-1] +l[-2])


if __name__ == '__main__':
    trial_runs = 30
    fibonacci_short = 'fib(1234)'
    fibonacci_norm = 'fibonacci(1234)'

    a =fib(123)
    print a, len(a)

    print "fibonacci standard method"
    print "timeit output %d times run fibonacci function:%s"%(trial_runs,fibonacci_norm)
    print timeit.timeit(stmt=fibonacci_norm,setup="from __main__ import fibonacci",number=trial_runs)

    print "fibonacci shortcut method"
    print "timeit output %d times run fib function:%s"%(trial_runs,fibonacci_short)
    print timeit.timeit(stmt=fibonacci_short,setup="from __main__ import fib",number=trial_runs)
    #T = timeit.Timer()
    #print fibonacci(123)
    #print l,len(l)
