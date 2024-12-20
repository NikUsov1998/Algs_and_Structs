from Geometry.PointInCircle import  point_in_circle
from Geometry.PointInTriangle import hitting_the_triangle
from Geometry.SegmentsIntersection import check_segment_intersection
from Geometry.domain.Segment import Segment

from Geometry.domain.Triangle import Triangle
from Geometry.domain.Point import Point
from Geometry.domain.Circle import Circle
from Geometry.domain.Vector import Vector

from Sorts.TournamentSort import tournament_sort
from Sorts.MergeSort  import merge_sort
from Sorts.BubbleSort import bubble_sort
from Sorts.SelectSort import select_sort
from Sorts.GnomeSort  import gnome_sort

import Geometry.PointInCircle

if __name__ == '__main__':
        list_1 = [5, 0, -2, 7, 3]
        print(list_1)
        bubble_sort(list_1)
        print(list_1)
        list_1 = [5, 0, -2, 7, 3]
        select_sort(list_1)
        print(list_1)
        list_1 = [5, 0, -2, 7, 3]
        gnome_sort(list_1)
        print(list_1)
        list_1 = [5, 0, -2, 7, 3]
        merge_sort(list_1)
        print(list_1)
        tournament_list = [11,14,5,10,13,15,12,7,4,3,6,1,8,9,2]
        tournament_sort(tournament_list)
        print(tournament_list)

        point_center: Point = Point(x=6, y=4)
        circle: Circle = Circle(point_center=point_center, radius=3)

        point1: Point = Point(x=8, y=3)
        point2: Point = Point(x=8, y=1)

        print(point_in_circle(circle=circle, point=point1))
        print(point_in_circle(circle=circle, point=point2))

        a: Point = Point(3,1)
        b: Point = Point(5,5)
        c: Point = Point(8,2)
        triangle: Triangle = Triangle(a,b,c)

        o: Point = Point(7,3)

        print(hitting_the_triangle(point=o, triangle=triangle))

        a: Point = Point(1,2)
        b: Point = Point(3,1)
        c: Point = Point(1,1)
        d: Point = Point(4,3)

        segment1: Segment = Segment(a,b)
        segment2: Segment = Segment(c,d)

        print(check_segment_intersection(segment1, segment2))

        a: Point = Point(1,2)
        b: Point = Point(3,3)
        c: Point = Point(1,1)
        d: Point = Point(4,3)

        segment1: Segment = Segment(a,b)
        segment2: Segment = Segment(c,d)

        print(check_segment_intersection(segment1, segment2))
