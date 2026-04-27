import math

from Geometry.domain.Circle import Circle
from Geometry.domain.Point import Point


def point_in_circle(circle: Circle, point: Point) -> bool:
    difference_x:float = point.x - circle.point_center.x
    difference_y:float = point.y - circle.point_center.y
    return (difference_x**2 + difference_y**2) <= circle.radius**2