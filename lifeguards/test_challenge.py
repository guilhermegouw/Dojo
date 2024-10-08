import pytest
from challenge import get_maximum_intervals_covered


@pytest.mark.parametrize(
    ("lifeguards", "expected"),
    [
        ([(1, 5), (7, 9), (11, 15)], 8),
        ([(1, 4), (5, 7), (8, 9)], 5),
        ([(0, 2), (3, 4), (5, 6), (7, 9)], 5),
        ([(1, 3), (4, 5), (6, 8)], 4),
        ([(1, 10), (15, 20), (21, 30)], 18),
    ],
)
def test_get_maximum_intervals_covered(lifeguards, expected):
    assert get_maximum_intervals_covered(lifeguards) == expected
