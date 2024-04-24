import pytest

from .challenge import non_constructible_change


@pytest.mark.parametrize(
    "coins,expected",
    [
        ([], 1),
        ([1], 2),
        ([1, 1], 3),
        ([1, 3], 2),
        ([1, 4], 2),
        ([1, 1, 4], 3),
    ],
)
def test_non_constructible_change(coins, expected):
    assert non_constructible_change(coins) == expected
