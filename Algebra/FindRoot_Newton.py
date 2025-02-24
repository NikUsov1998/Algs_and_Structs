import math
from typing import Callable

from Algebra.domain.Derivative_Calculation import derivative_calculation_5


def find_root_Newton(f: Callable, x_0: float, err:float) -> float:
    while True:
        x:float = x_0 - f(x_0)/derivative_calculation_5(f, x_0, err/2)
        if abs(x - x_0) < err:
            return x
        x_0 = x

def f(x:float): return x**2 - math.exp(x)

def test_find_root_Newton():
    print('\n')
    x_0: float = 0
    err: float = 0.000000000000001
    print(find_root_Newton(f, x_0, err))