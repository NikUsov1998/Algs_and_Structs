import math
from typing import Callable

def derivative_calculation_2(f: Callable, x: float, delta_x: float) -> float:
    # first: float = f(x+delta_x)
    # second: float = f(x-delta_x)
    # third: float = 2*delta_x
    # result: float = (first - second) / third
    return (f(x+delta_x) - f(x-delta_x))/(2*delta_x)

def derivative_calculation_5(func: Callable, x: float, delta_x: float) -> float:
    # first: float = f(x - 2 * delta_x)
    # second: float = 8 * f(x - delta_x)
    # third: float = 8 * f(x + delta_x)
    # forth: float = f(x + 2 * delta_x)
    # fifth: float = (12*delta_x)
    # result: float = (first - second + third - forth)/fifth
    # return result
    return (func(x - 2 * delta_x) - (8 * func(x - delta_x)) + (8 * func(x + delta_x)) - func(x + 2 * delta_x))/(12 * delta_x)

def f(x:float): return x**2 - math.exp(x)

def test_derivative_calculation_2():
    x:float = 0
    delta_x: float = 0.001
    print('\n')
    while(x<=2):
        print(round(x, 4), '\t', derivative_calculation_2(f,x,delta_x))
        x += 0.2

def test_derivative_calculation_5():
    x:float = 0
    delta_x: float = 0.001
    print('\n')
    while(x<=2):
        print(round(x, 4), '\t', derivative_calculation_5(f,x,delta_x))
        x += 0.2
