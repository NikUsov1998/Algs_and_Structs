import pytest

from Geometry.domain.Point import Point
from Geometry.domain.Segment import Segment
from Geometry.SegmentsIntersection import check_segment_intersection

@pytest.fixture
def segment_ab():
    a: Point = Point(1, 2)
    b: Point = Point(3, 1)
    segment_ab: Segment = Segment(a, b)
    return segment_ab

@pytest.fixture
def segment_ae():
    a: Point = Point(1, 2)
    e: Point = Point(3, 3)
    segment_ae: Segment = Segment(a,e)
    return segment_ae

@pytest.fixture
def segment_cd():
    c: Point = Point(1, 1)
    d: Point = Point(4, 3)
    segment_cd: Segment = Segment(c, d)
    return segment_cd

def test_check_segment_intersects(segment_ab, segment_cd):
    assert check_segment_intersection(segment1=segment_ab, segment2=segment_cd)

def test_check_segment_not_intersects(segment_ae, segment_cd):
    assert not check_segment_intersection(segment1=segment_ae, segment2=segment_cd)
