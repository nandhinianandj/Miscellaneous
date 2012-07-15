#include "math.h"
#include <stdio.h>

long double factorial(long n)
{
  if (n <= 1)
    return 1;
  else
    return n*factorial(n-1);
}


double long_factorial(double n)
{
  return exp(lgamma(n));
}

void main()
{
  printf("%lf\n",long_factorial(1000));
}
