import pytest
from Sorts.SelectSort import select_sort

@pytest.fixture
def list_1():
    list_1:list[int] = [5, 0, -2, 7, 3]
    return list_1

def test_select_sort(list_1):
    select_sort(list_1)
    assert list_1 == [-2, 0, 3, 5, 7]
