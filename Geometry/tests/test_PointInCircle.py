import pytest
from Geometry.PointInCircle import point_in_circle
from Geometry.domain.Point import Point
from Geometry.domain.Circle import Circle

@pytest.fixture
def circle():
    point_center: Point = Point(x=6, y=4)
    radius: float = 3
    circle: Circle = Circle(point_center=point_center, radius=radius)
    return circle

@pytest.fixture
def point_in():
    point_in: Point = Point(x=8, y=3)
    return point_in

@pytest.fixture
def point_out():
    point_out: Point = Point(x=8, y=1)
    return point_out

def test_point_in_circle(circle, point_in):
    assert point_in_circle(circle=circle, point=point_in)

def test_point_not_in_circle(circle, point_out):
    assert not point_in_circle(circle=circle, point=point_out)