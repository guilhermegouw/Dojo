import pytest

from .challenge import largest_product


@pytest.mark.parametrize(
    "array,expected",
    [
        ([1, 2, 3], 6),
        ([1, 2, 3, 4], 24),
        ([1, 2, 3, 4, 5], 60),
        ([1, 2, 3, 4, 5, 6], 120),
        ([1, 2, 3, 4, 5, 6, 7], 210),
    ],
)
def test_largest_product(array, expected):
    assert largest_product(array) == expected
