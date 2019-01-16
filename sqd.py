# Решение квадратного уравнения

def solve_quad(b, c):
    import numpy
    return numpy.roots([1, b, c])



# Test

from numpy import allclose

variants = [{'b': 4.0, 'c': 3.0},
            {'b': 2.0, 'c': 1.0},
            {'b': 0.5, 'c': 4.0},
            {'b': 1e10, 'c': 3.0},
            {'b': -1e10, 'c': 4.0},]

for var in variants:
    x1, x2 = solve_quad(**var)
    print(allclose(x1*x2, var['c']))