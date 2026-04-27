import math
from typing import Callable

def find_root(equation: Callable, a: float, b: float, err: float) -> float:
    if equation(a)*equation(b) >= 0:
        raise Exception("Initial approximation error")
    c1: float = a
    while True:
        a_values: float = equation(a)
        b_values: float = equation(b)
        c2: float = a - (a_values*(a-b))/(a_values-b_values)
        c_values: float = equation(c2)
        if abs(c1-c2) < err:
            return c2
        if (a_values < 0 < c_values) or (a_values > 0 > c_values):
            b = c2
        else:
            a = c2
        c1=c2

def F(x): return x**2 - math.exp(x)

def test_chord_method():
    a = -1
    b = 1
    err = 0.1
    root = find_root(F, a, b, err)
    print(root)
    print(F(root))