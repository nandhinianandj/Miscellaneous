from functools import lru_cache, reduce
import math

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def max_prime_factors(n):
    print(list(primes_sieve2(int(math.sqrt(n)))))
    prime_factors = [x for x in primes_sieve2(int(math.sqrt(n))) if n%x ==0]

    return max(prime_factors)

print(max_prime_factors(600851475143))
