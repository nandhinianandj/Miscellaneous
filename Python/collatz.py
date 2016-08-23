import math
def is_pow_of_2(num):
    """
    @return: returns power value if not returns False
    """
    return num != 0 and ((num & (num - 1)) == 0)
    # import math
    # res = math.log(n, 2)
    # if (res - int(res)) == 0:
    #    return res
    #else:
    #    return false

def collatz(n, cache):
    if n == 1:
        return 1
    elif n in cache.keys():
        return cache[n]
    elif n % 2 == 0:
        if is_pow_of_2(int(n)):
            cache[n] = 1 + math.log(n,2)
            return cache[n]
        else:
            cache[n] = 1 + collatz(n/2, cache)
    else:
        cache[n] = 1 + collatz(3 * n + 1, cache)
    return cache[n]

def main(n1, n2):
    cache = {}
    lengths = []
    m = -1
    for x in range(n1, n2):
        length = collatz(x, cache)
        cache[x] = length
        lengths.append(length)
        if (length > m):
            m = length
            the_one = x

    print(n1, n2, int(max(lengths)))

if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()')
    import sys
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2]) if len(sys.argv) > 2 else n1 + 1
    main(n1,n2 )
