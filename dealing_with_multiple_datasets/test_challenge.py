from .challenge import products_between_arrays, products_between_arrays2

import pytest


@pytest.mark.parametrize(
    "array1,array2,expected",
    [
        ([1], [10], [10]),
        ([1, 2], [10], [10, 20]),
        ([1, 2], [10, 100], [10, 100, 20, 200]),
        ([1, 2, 3], [10, 100], [10, 100, 20, 200, 30, 300]),
        (
            [1, 2, 3],
            [10, 100, 1000],
            [10, 100, 1000, 20, 200, 2000, 30, 300, 3000],
        ),
    ],
)
def test_products_between_arrays(array1, array2, expected):
    assert products_between_arrays(array1, array2) == expected


@pytest.mark.parametrize(
    "array1,array2,expected",
    [
        ([1], [10], [10]),
        ([1, 2], [10], [10, 20]),
        ([1, 2], [10, 100], [10, 100, 20, 200]),
        ([1, 2, 3], [10, 100], [10, 100, 20, 200, 30, 300]),
        (
            [1, 2, 3],
            [10, 100, 1000],
            [10, 100, 1000, 20, 200, 2000, 30, 300, 3000],
        ),
    ],
)
def test_products_between_arrays2(array1, array2, expected):
    assert products_between_arrays2(array1, array2) == expected
