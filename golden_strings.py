
from sympy.mpmath import mp, fraction

a = "1"
b = "10"
for i in range(10):
   b, a = b+a, b
   print(b)

   n = len(b)
   mp.dps = n
   denom = 2**n
   num = int(b, 2)

   rabbit = fraction(num, denom)
   print(rabbit)
