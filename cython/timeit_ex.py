def main():
    timeit.timeit('import cyfib;cyfib.fib(3245)')
    timeit.timeit('import fib;fib.fib(3424)')

if __name__='__main__':
    main()
