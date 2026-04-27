import pytest
from Sorts.TournamentSort import tournament_sort

@pytest.fixture
def tournament_list():
    tournament_list: list[int] = [11, 14, 5, 10, 13, 15, 12, 7, 4, 3, 6, 1, 8, 9, 2]
    return tournament_list

def test_tournament_sort(tournament_list):
    tournament_sort(tournament_list)
    assert tournament_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
