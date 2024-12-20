from Geometry.domain.Point import Point

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
