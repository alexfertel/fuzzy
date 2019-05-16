from math import exp

def triangular(a, m, b, x):
    if a <= x <= m:
        return (x - a) / (m - a)
    if m <= x <= b:
        return (b - x) / (b - m)
    return 0

def trapezoidal(a, b, c, d, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    if c <= x <= d:
        return (d - x) / (d - c)
    return 1 if b <= x <= c else 0

def gaussian(c, d, x):
    n = x - c
    return exp( -( n * n ) / ( 2 * d * d ) )

def r_func(c, d, x):
    return trapezoidal(float('-inf'), float('-inf'), c, d, x)

def l_func(a, b, x):
    return trapezoidal(a, b, float('inf'), float('inf'), x)
