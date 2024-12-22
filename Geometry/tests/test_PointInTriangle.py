import pytest

from Geometry.domain.Point import Point
from Geometry.domain.Triangle import Triangle
from Geometry.PointInTriangle import hitting_the_triangle

@pytest.fixture
def triangle():
    a: Point = Point(3, 1)
    b: Point = Point(5, 5)
    c: Point = Point(8, 2)
    triangle: Triangle = Triangle(a, b, c)
    return triangle

@pytest.fixture()
def point_o():
    o: Point = Point(7, 3)
    return o

def test_hitting_the_triangle(triangle, point_o):
    assert hitting_the_triangle(triangle=triangle, point=point_o)
