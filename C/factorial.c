// Factorial is a special case of the log-gamma function
// https://en.wikipedia.org/wiki/Gamma_function
long int fac(unsigned long int n) {
	    return lround(exp(lgamma(n+1)));
}
