def pentagon(n):
    return n*(3*n - 1) / 2

def collatz(n, cache={}):
    import collatz
    return collatz.collatz(n, cache)
