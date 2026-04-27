import math

from Geometry.domain.Point import Point
from Geometry.PointInTriangle import vector_cross_product
from Geometry.domain.Vector import Vector
from Geometry.domain.Segment import Segment

def range_intersection(range_1_s: float, range_1_e:float, range_2_s: float, range_2_e:float) -> float:
    if range_1_s > range_1_e:
        range_1_s, range_1_e = range_1_e, range_1_s
    if range_2_s > range_2_e:
        range_2_s, range_2_e = range_2_e, range_2_s
    return max(range_1_s, range_2_s) <= min(range_1_e, range_2_e)

def bounding_box(segment_1: Segment, segment_2: Segment) -> float:
    x1: float = segment_1.start_point.x
    x2: float = segment_1.end_point.x
    x3: float = segment_2.start_point.x
    x4: float = segment_2.end_point.x
    y1: float = segment_1.start_point.y
    y2: float = segment_1.end_point.y
    y3: float = segment_2.start_point.y
    y4: float = segment_2.end_point.y
    return range_intersection(x1,x2,x3,x4) and range_intersection(y1,y2,y3,y4)

def check_segment_intersection(segment1: Segment, segment2:Segment) -> bool:
    if not bounding_box(segment1, segment2):
        return False
    vector_ab: Vector = Vector(segment1.start_point, segment1.end_point)
    vector_ac: Vector = Vector(segment1.start_point, segment2.start_point)
    vector_ad: Vector = Vector(segment1.start_point, segment2.end_point)

    vector_cd: Vector = Vector(segment2.start_point, segment2.end_point)
    vector_ca: Vector = Vector(segment2.start_point, segment1.start_point)
    vector_cb: Vector = Vector(segment2.start_point, segment1.end_point)

    d1:float = vector_cross_product(vector_ab, vector_ac)
    d2:float = vector_cross_product(vector_ab, vector_ad)
    d3:float = vector_cross_product(vector_cd, vector_ca)
    d4:float = vector_cross_product(vector_cd, vector_cb)

    if((d1 <= 0 <= d2) or (d1 >= 0 >= d2)) and ((d3 <= 0 <= d4) or (d3 >= 0 >= d4)):
        return True
    return False

