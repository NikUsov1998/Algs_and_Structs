import pytest
from Sorts.BubbleSort import bubble_sort

@pytest.fixture
def list_1():
    list_1:list[int] = [5, 0, -2, 7, 3]
    return list_1

def test_bubble_sort(list_1):
    bubble_sort(list_1)
    assert list_1 == [-2, 0, 3, 5, 7]
