# -*- coding: utf-8 -*-
def compose2(f, g):
    return lambda x: f(g(x))

import functools

def compose(*functions):
    def compose2(f, g):
        return lambda x: f(g(x))
    return functools.reduce(compose2, functions, lambda x: x)

def sub(a, b):
    return a - b

compose = λ *fs: reduce(λ f, g: λ *x: f(*g(*x)), fs)

pipeline = compose(functools.partial(sub, b=4), operator.neg)
