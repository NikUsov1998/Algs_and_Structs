from Geometry.domain.Point import Point

class Segment:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.__start_point:Point = start_point
        self.__end_point:Point = end_point

    def __str__(self) -> str:
        return f"Segment[start = {self.__start_point}, end = {self.__end_point}"

    @property
    def start_point(self) -> Point:
        return self.__start_point

    @property
    def end_point(self) -> Point:
        return self.__end_point
