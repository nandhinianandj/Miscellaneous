def digits(n):
    s = set()
    while n > 0:
        s.add(n%10)
        n /= 10
    return s


def main(n,m):
    for i in range(n, m):
        p = 2**i
        if 7 not in digits(p):
            print i, p

if __name__ == '__main__':
    import sys
    n,m = int(sys.argv[1]),int(sys.argv[2])
    main(n,m)
