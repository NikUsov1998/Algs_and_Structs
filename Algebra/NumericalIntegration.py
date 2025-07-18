from typing import Callable


class SquareMethod:
    @staticmethod
    def left_square(func: Callable, x2: float, x1: float, n: int):
        delta_x: float = (x2 - x1)/n
        result: float = 0.0
        for i in (range(n-1)):
            result += func(x1+i*delta_x)*delta_x
        return result

    @staticmethod
    def midpoint(func: Callable, x2: float, x1: float, n: int) -> float:
        delta_x: float = (x2 - x1)/n
        result: float = 0.0
        for i in (range(n)):
            result += func(x1+(i+0.5)*delta_x)*delta_x
        return result

    @staticmethod
    def right_square(func: Callable, x2: float, x1: float, n: int):
        delta_x: float = (x2 - x1)/n
        result: float = 0.0
        for i in (range(n)):
            result += func(x1+i*delta_x)*delta_x
        return result


class TrapezoidMethod:
    @staticmethod
    def trapeziod(func: Callable, x2: float, x1: float, n: int) -> float:
        delta_x: float = (x2 - x1)/n
        result: float = 0.0
        for i in (range(n)):
            first_value: float = func(x1 + i * delta_x)
            second_value: float = func(x1 + (i+1) * delta_x)
            result += (first_value + second_value) / 2.0 * delta_x
        return result

class SimpsonMethod:
    @staticmethod
    def simpson(func: Callable, x2: float, x1: float, n: int) -> float:
        delta_x: float = (x2-x1)/n
        result: float = 0.0
        for i in (range(n)):
            fun_sum = func(x1 + i * delta_x)
            fun_sum += 4*func(x1+(i+0.5)*delta_x)
            fun_sum += func(x1+(i+1)*delta_x)
            fun_sum *= delta_x/6.0
            result += fun_sum
        return result

def f(x): return x**2

def test_simpson():
    x1: int = 1
    x2: int = 2
    result: float = SimpsonMethod.simpson(f,x2,x1,100000)
    print('\n',result)
    print(7/3)

def test_trapeziod():
    x1: int = 1
    x2: int = 2
    result: float = TrapezoidMethod.trapeziod(f, x2, x1, 100000)
    print('\n',result)
    print(7/3)

def test_midpoint():
    x1: int = 1
    x2: int = 2
    result: float = SquareMethod.midpoint(f, x2, x1, 100000)
    print('\n',result)
    print(7/3)

def test_left_square():
    x1: int = 1
    x2: int = 2
    result: float = SquareMethod.left_square(f, x2, x1, 100000)
    print('\n',result)
    print(7/3)

def test_right_square():
    x1: int = 1
    x2: int = 2
    result: float = SquareMethod.right_square(f, x2, x1, 100000)
    print('\n',result)
    print(7/3)
