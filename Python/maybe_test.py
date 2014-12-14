from pymonad import *

def testFunc(a,b):
    return Maybe.unit(a/b)

def main():
    print testFunc(1,1)

if __name__ == '__main__':
    main()
