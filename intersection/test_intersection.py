import pytest

from intersection import intersection, force_intersection


@pytest.mark.parametrize(
    "first_array,second_array,expected",
    [
        ([1, 2, 3], [2, 3, 4], [2, 3]),
        ([1, 2, 3], [3, 4], [3]),
        ([1, 2, 3], [4, 5, 6], []),
        ([], [], []),
        ([], [1, 2, 3], []),
        ([1, 2, 3], [], []),
        ([1, 1, 2, 3, 4, 5], [1, 4, 5, 6, 7, 8], [1, 4, 5]),
    ],
)
def test_intersection(first_array, second_array, expected):
    assert intersection(first_array, second_array) == expected


@pytest.mark.parametrize(
    "first_array,second_array,expected",
    [
        ([1, 2, 3], [2, 3, 4], [2, 3]),
        ([1, 2, 3], [3, 4], [3]),
        ([1, 2, 3], [4, 5, 6], []),
        ([], [], []),
        ([], [1, 2, 3], []),
        ([1, 2, 3], [], []),
        ([1, 1, 2, 3, 4, 5], [1, 4, 5, 6, 7, 8], [1, 4, 5]),
    ],
)
def test_force_intersection(first_array, second_array, expected):
    assert force_intersection(first_array, second_array) == expected
