import math
from Geometry.domain.Point import Point

class Triangle:
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point) -> None:
        self.__vertex1: Point = vertex1
        self.__vertex2: Point = vertex2
        self.__vertex3: Point = vertex3

    def __str__(self) -> str:
        return f"Triangle[vertex 1 = {self.__vertex1}, vertex 2 = {self.__vertex2}, vertex 3 = {self.__vertex3}]"

    @property
    def vertex1(self) -> Point:
        return self.__vertex1

    @vertex1.setter
    def vertex1(self, vertex1: Point) -> None:
        self.__vertex1 = vertex1

    @property
    def vertex2(self) -> Point:
        return self.__vertex2

    @vertex2.setter
    def vertex2(self, vertex2: Point) -> None:
        self.__vertex2 = vertex2

    @property
    def vertex3(self) -> Point:
        return self.__vertex3

    @vertex3.setter
    def vertex3(self, vertex3:Point) -> None:
        self.__vertex3 = vertex3
