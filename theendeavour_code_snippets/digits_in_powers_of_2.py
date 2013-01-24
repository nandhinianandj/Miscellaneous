def digits(n):
    s = set()
    while n > 0:
        s.add(n%10)
        n /= 10
    return s

def seven_in_digits_str(n):
    s = str(n)
    if '7' not in s:
        return "No 7, %s",s
    else:
        return False

def main1(n,m):
    p = bytearray(math.ceil(max(n,m)/8))
    for i in range(n,m):
        pass
def main(n,m):
    for i in range(n, m):
        p = 2**i
        if seven_in_digits_str(p):
            print i, p

if __name__ == '__main__':
    import sys
    n,m = long(sys.argv[1]),long(sys.argv[2])
    main(n,m)
