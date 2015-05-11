from sympy import Symbol, solve, solve_univariate_inequality, sympify, solve_rational_inequality, Poly
x = Symbol('x')
solve_univariate_inequality(x+4 > 0, x, relational=False)
solve_univariate_inequality((x+4)*(x-2)*(x-7) > 0, x, relational=False)
solve_univariate_inequality((x - 5)**2*(x - 1)*(x + 3) <= 0, x, relational=False)
solve_univariate_inequality((x**2+2)*(x+5)**3*(4-2*x)*(x**2)*(x-6) <= 0, x, relational=False)
s5 = solve_univariate_inequality(sympify('-4*(x+3)>24'), x, relational=False)
solve_rational_inequalities([[((Poly(x-1), Poly(x+2)), '>')]])
solve_rational_inequalities([[((Poly(x-4)-4*Poly(x+5), Poly(x+5)), '<')]])
