import pytest
from challenge import get_ball_location


@pytest.mark.parametrize(
    "swaps, expected",
    [
        ("A", "middle"),
        ("B", "left"),
        ("C", "right"),
        ("AC", "middle"),
        ("BC", "right"),
        ("ABC", "left"),
        ("CBA", "left"),
        ("ACB", "right"),
        ("BAC", "middle"),
        ("BCA", "right"),
    ],
)
def test_get_ball_location(swaps, expected):
    assert get_ball_location(swaps) == expected
