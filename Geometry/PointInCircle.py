import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.__x: float = x
        self.__y: float = y

    def __str__(self) -> str:
        return f"Point[x={self.__x}, y={self.__y}]"

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, new_x: float) -> None:
        self.__x = new_x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, new_y:float) -> None:
        self.__y = new_y


class Circle:
    def __init__(self, point_center: Point, radius: float) -> None:
        self.__point_center: Point = point_center
        self.__radius:float = radius

    def __str__(self) -> str:
        return f"Circle[center = {self.__point_center}, radius={self.__radius}]"

    @property
    def point_center(self) -> Point:
        return self.__point_center

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius) -> None:
        self.__radius = radius

def point_in_circle(circle: Circle, point: Point) -> float:
    difference_x:float = point.x - circle.point_center.x
    difference_y:float = point.y - circle.point_center.y
    return (difference_x**2 + difference_y**2) <= circle.radius**2