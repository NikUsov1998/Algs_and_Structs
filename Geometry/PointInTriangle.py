import math
from Geometry.domain.Point import Point
from Geometry.domain.Vector import Vector
from Geometry.domain.Triangle import Triangle

def vector_cross_product(vector1: Vector, vector2: Vector) -> float:
    return vector1.x_component * vector2.y_component - vector2.x_component * vector1.y_component

def hitting_the_triangle(point: Point, triangle: Triangle) -> bool:
    vertex_1: Point = triangle.vertex1
    vertex_2: Point = triangle.vertex2
    vertex_3: Point = triangle.vertex3

    vector1: Vector = Vector(vertex_1, point)
    vector2: Vector = Vector(vertex_2, point)
    vector3: Vector = Vector(vertex_3, point)

    product1:float = vector_cross_product(vector1, Vector(vertex_1, vertex_2))
    product2:float = vector_cross_product(vector2, Vector(vertex_2, vertex_3))
    product3:float = vector_cross_product(vector3, Vector(vertex_3, vertex_1))
    return (product1 >= 0 and product2 >=0 and product3 >=0) or (product1 <=0 and product2 <=0 and product3 <=0)

