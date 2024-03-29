import pytest

from .challenge import merge, merge_2


@pytest.mark.parametrize(
    "array_1, array_2, expected",
    [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 3, 5], [4, 5, 6, 7, 8], [1, 3, 4, 5, 5, 6, 7, 8]),
        ([], [], []),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([1, 3, 7, 10], [4, 6], [1, 3, 4, 6, 7, 10]),
    ],
)
def test_merge(array_1, array_2, expected):
    assert merge(array_1, array_2) == expected


@pytest.mark.parametrize(
    "array_1, array_2, expected",
    [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 3, 5], [4, 5, 6, 7, 8], [1, 3, 4, 5, 5, 6, 7, 8]),
        ([], [], []),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([1, 3, 7, 10], [4, 6], [1, 3, 4, 6, 7, 10]),
    ],
)
def test_merge_2(array_1, array_2, expected):
    assert merge_2(array_1, array_2) == expected
