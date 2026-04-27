import math
from Geometry.domain.Point import Point
from Geometry.domain.Circle import Circle

def intersection_of_circles(circle_1: Circle, circle_2:Circle) -> bool:
    x_distance: float = circle_1.point_center.x - circle_2.point_center.x
    y_distance: float = circle_1.point_center.y - circle_2.point_center.y
    r1:float = circle_1.radius
    r2:float = circle_2.radius
    return (r2-r1)**2 <= (x_distance**2 + y_distance**2) <= (r2+r1)**2