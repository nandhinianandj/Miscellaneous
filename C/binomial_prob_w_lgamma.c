#include <math.h>
#include <stdio.h>

double long_factorial(double n)
{
  return exp(lgamma(n));
}


double probability(double p, double q, int m, int n)
{
  double temp = lgamma(m + n + 1.0);
  temp -= lgamma(n + 1.0) + lgamma(m + 1.0);
  temp += m*log(p) + n*log(q);
  return exp(temp);
}
