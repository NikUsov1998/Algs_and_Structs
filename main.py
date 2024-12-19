from Geometry.PointInCircle import Point, Circle, point_in_circle
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
