# cdef double f(double x) except? -2:
#     return x**2-x

# def f(double x):
#     return x**2-x

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

# def py_integrate_f(double a, double b, int N):
#     cdef int i
#     dx = (b-a)/N
#     for i in range(N):
#         s += f(a+i*dx)
#     return s * dx

def main():
    py_integrate_f(0.12, 0.44, 25)
    pass

if __name__=="__main__":
    main()
