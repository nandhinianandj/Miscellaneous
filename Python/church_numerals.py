#Copied from (https://gist.github.com/2438498)
zero = lambda f: lambda x: x

succ = (lambda n: lambda f: lambda x: f(n(f)(x)))

one = succ(zero)

add = (lambda m: lambda n: lambda f: lambda x: n(f(m(f)(x))))

mult = (lambda m: lambda n: lambda f: lambda x: n(m(f))(x))

exp = lambda m: lambda n: n(m)

plus1 = lambda x:x+1

church2int = lambda n: n(plus1)(0)

def int2church(i):
    if i == 0:
        return zero
    else:
        return succ(int2church(i-1))


def peval(s):
    print s, ' = ',eval(s)


peval('church2int(zero)')
peval('church2int(succ(zero))')

peval('church2int(one)')
peval('church2int(succ(one))')
peval('church2int(succ(succ(one)))')

peval('church2int(succ(succ(succ(one))))')

peval('church2int(add(one)(succ(one)))')
peval('church2int(add(succ(one)) (succ(one)))')
peval('church2int(add(succ(one)) (succ(one)))')

peval('church2int(mult(succ(one))(succ(one)))')
peval('church2int(exp(succ(one))(succ(one)))')

peval('church2int(int2church(0))')

peval('church2int(int2church(1))')
peval('church2int(int2church(111))')

c232 = int2church(232)
c421 = int2church(421)

peval('church2int(mult(c232)(c421))')

print "232*421 = ",232*421

c2 = int2church(2)
c10 = int2church(10)

peval('church2int(exp(c2)(c10))')
print '2**10 = ',2 **10




