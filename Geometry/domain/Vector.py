from abc import abstractmethod

from Geometry.domain.Point import Point
from typing import Self

class Vector:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.__start_point: Point = start_point
        self.__end_point: Point = end_point
        self.__x_component:float = end_point.x - start_point.x
        self.__y_component:float = end_point.y - start_point.y

    def __str__(self) -> str:
        return f"Vector [start = {self.__start_point}, end = {self.__end_point}]"

    #@abstractmethod
    #def vector_cross_product(vector1: Self, vector2: Self) -> float:
    #    return vector1.x_component * vector2.y_component - vector2.x_component * vector1.y_component

    @property
    def start_point(self) -> Point:
        return self.__start_point

    @property
    def end_point(self) -> Point:
        return self.__end_point

    @property
    def x_component(self) -> float:
        return self.__x_component

    @property
    def y_component(self) -> float:
        return self.__y_component