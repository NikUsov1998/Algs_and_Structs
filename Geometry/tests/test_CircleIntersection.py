import pytest
from Geometry.domain.Point import Point
from Geometry.domain.Circle import Circle
from Geometry.CircleIntersection import intersection_of_circles

@pytest.fixture
def circle1():
    a: Point = Point(4, 3)
    r1: int = 2
    circle1: Circle = Circle(a, r1)
    return circle1

@pytest.fixture
def circle2():
    b: Point = Point(7, 5)
    r2: float = 3
    circle2: Circle = Circle(b, r2)
    return circle2

@pytest.fixture
def circle3():
    b: Point = Point(9, 6)
    r2: float = 3
    circle3: Circle = Circle(b, r2)
    return circle3

@pytest.fixture
def circle4():
    b: Point = Point(4, 4)
    r2: float = 3.2
    circle4: Circle = Circle(b, r2)
    return circle4

def test_intersection_of_circles(circle1, circle2):
    assert intersection_of_circles(circle_1=circle1, circle_2=circle2)

def test_circles_not_intersects(circle1,circle3):
    assert not intersection_of_circles(circle_1=circle1, circle_2=circle3)

def test_first_circle_inside_second(circle1, circle4):
    assert not intersection_of_circles(circle_1=circle1, circle_2=circle4)
