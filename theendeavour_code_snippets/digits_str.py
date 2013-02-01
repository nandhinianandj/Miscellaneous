
def main(n,m):
    for i in xrange(n, m):
        p = 2**i
        if '7' not in str(p):
    	    print i, p

if __name__=='__main__':
    import sys
    main(long(sys.argv[1]),long(sys.argv[2]))
