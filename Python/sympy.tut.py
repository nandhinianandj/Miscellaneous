# https://github.com/sympy/sympy/wiki/Quick-examples

from sympy.abc import x,y
e = x + y + x
print e


from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = map(Function, 'fgh')


Rational(3,2)*pi + exp(I*x) / (x**2 + y)

x = Symbol('x')
exp(I*x).subs(x,pi).evalf()    #doctest: +SKIP


expr = x + 2*y
expr.__class__
expr.args
