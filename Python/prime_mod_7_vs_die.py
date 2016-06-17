from sympy import prime
from random import random
from math import ceil
from scipy.stats import chi2

def chisq_stat(O, E):
    return sum( [(o - e)**2/e for (o, e) in zip(O, E)] )

num_sides = 6
modulus = num_sides + 1

# Find the index of the smallest prime bigger than num_sides
index = 1
while prime(index) <= modulus:
	index += 1

# Number of samples
N = 1000000

observed_primes = [0]*modulus
observed_random = [0]*modulus

for i in range(index, N+index):
	m = prime(i) % modulus
	observed_primes[m] += 1
	m = int(ceil(random()*num_sides))
	observed_random[m] += 1

expected = [N/num_sides for i in range(1, modulus)]

ch = chisq_stat(observed_primes[1:], expected[1:])
print(ch)
print(chi2.cdf(ch, num_sides-1), chi2.sf(ch, num_sides-1))

ch = chisq_stat(observed_random[1:], expected[1:])
print(ch)
print(chi2.cdf(ch, num_sides-1), chi2.sf(ch, num_sides-1))
