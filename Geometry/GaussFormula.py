from Geometry.domain.Point import Point
import math

def calculate_square(points: list[Point]) -> float:
    n: int = len(points)
    s = 0
    for i in range(n):
        point_a: Point = points[i]
        point_b: Point = points[(i+1) % n]
        s += point_a.x * point_b.y - point_b.x * point_a.y
    return 1/2 * abs(s)