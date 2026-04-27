import pytest

from Geometry.domain.Point import Point
from Geometry.GaussFormula import calculate_square

@pytest.fixture
def figure_vertex_list():
    point_a: Point = Point(2, 2)
    point_b: Point = Point(4, 4)
    point_c: Point = Point(6, 4)
    point_d: Point = Point(7, 2)
    points: list[Point] = [point_a, point_b, point_c, point_d]
    return points

def test_calculate_square(figure_vertex_list):
    s: float = calculate_square(figure_vertex_list)
    assert s == 7
