from sympy import Symbol

MAX_ITERS = 10000
DIVERGE_TOLERANCE = 0.5
SIG_DIGITS = 15

def is_diverging(poly, num):
    global MAX_ITERS, SIG_DIGITS, DIVERGE_TOLERANCE
    numbers = list()
    old = num
    new = old
    for i in range(MAX_ITERS):
        x = S(new)
        new = poly.evalf(SIG_DIGITS)
        if (new - old) > DIVERGE_TOLERANCE:
            return True
    return False

def get_julia(polynomial, ranges):
    """
        Return a  julia set of a given polynomial
        @params:
            @polynomial:
            @ranges:
    """
    assert isinstance(polynomial, Symbol)
    def func(polynomial, ranges):
        divergers = list()
        convergers = list()
        for item in ranges:
            if is_diverging(polynomial(item)):
                divergers.append(item)
            else:
                convergers.append(item)
    pass

