from Sorts.BubbleSort import BubbleSort
from Sorts.SelectSort import SelectSort
from Sorts.GnomeSort  import GnomeSort

if __name__ == '__main__':
        list_1 = [5, 0, -2, 7, 3]
        print(list_1)
        BubbleSort(list_1)
        print(list_1)
        list_1 = [5, 0, -2, 7, 3]
        SelectSort(list_1)
        print(list_1)
        list_1 = [5, 0, -2, 7, 3]
        GnomeSort(list_1)
        print(list_1)
