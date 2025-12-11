from typing import Union


def liner_interpolation_two_points(x1: float, y1: float, x2: float, y2: float, x: float) -> float:
    y: float = (x-x1)*(y1-y2)/(x1-x2)+y1
    return y

def linear_interpolation(x_values: list[Union[int, float]], y_values: list[Union[int, float]], x: int | float):
    for i in range(len(x_values)-1):
        if x_values[i] <= x <= x_values[i + 1]:
            x1: Union[int, float] = x_values[i]
            x2: Union[int, float] = x_values[i+1]
            y1: Union[int, float] = y_values[i]
            y2: Union[int, float] = y_values[i+1]
            return liner_interpolation_two_points(x1, y1, x2, y2, x)
    return None

def test_linear_interpolation():
    height = [0.15, 0.3, 1.5, 3.0, 6.1, 7.6, 9.1, 10.7]
    age = [9, 13, 27, 41, 83, 107, 131, 157]
    x = 5
    y = linear_interpolation(height, age, x)
    print(y)