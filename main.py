from Geometry.CircleIntersection import intersection_of_circles
from Geometry.GaussFormula import calculate_square
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


def main() -> int:

        return 0

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




