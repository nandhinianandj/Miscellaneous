import collatz
def pentagon(n):
    return n*(3*n - 1) / 2

def collatz(n, cache={}):
    return collatz.collatz(n, cache)
