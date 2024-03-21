import pytest

from .challenge import get_all_the_products


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1], []),
        ([1, 2], [2]),
        ([1, 2, 3], [2, 3, 6]),
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 8, 10, 12, 15, 20]),
    ],
)
def test_get_all_the_products(numbers, expected):
    assert get_all_the_products(numbers) == expected
