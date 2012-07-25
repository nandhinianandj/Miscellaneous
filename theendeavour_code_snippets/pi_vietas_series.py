from math import sqrt
prod = 1.0
radic = 0.0

for i in range(100):
    radic = sqrt(2.0 + radic)
    prod *= 0.5*radic
    print 2.0/prod

