import math
from typing import Callable


def find_root_segment_half(equation: Callable, a: float, b: float, err: float) -> float:
    if equation(a)*equation(b) >= 0:
        raise Exception("Initial approximation error")
    while True:
        c:float = (a+b)/2
        a_values:float = equation(a)
        b_values:float = equation(b)
        c_values:float = equation(c)
        if abs(c_values) < err:
            return c
        if a_values*c_values < 0:
            b = c
        else:
            a = c

def F(x) -> float: return x**2 - math.exp(x)

def test_frsh():
    a = -1
    b = 1
    err = 0.1
    root = find_root_segment_half(F, a, b, err)
    assert root == -0.75