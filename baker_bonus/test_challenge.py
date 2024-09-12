import pytest
from challenge import get_total_bonus


@pytest.mark.parametrize(
    "f, d, sales, expected",
    [
        (2, 4, [[1, 2, 3, 4], [5, 6, 7, 8]], 2),
        (2, 4, [[1, 2, 3, 4], [5, 6, 7, 10]], 0),
    ],
)
def test_get_total_bonus(f, d, sales, expected):
    assert get_total_bonus(f, d, sales) == expected


"""
Exploring the problem:

Bonus conditions:

1. For every day on which the total sales across all franchisees is
a multiple of 13 that multiple will be given as bonuses.
For example:

day 1:
f1 = 1
f2 = 5
total = 1 + 5 = 6
bonus = 6 / 13 = 0

day 2:
f1 = 2
f2 = 6
total = 2 + 6 = 8
bonus = 8 / 13 = 0

day 3:
f1 = 3
f2 = 7
total = 3 + 7 = 10
bonus = 10 / 13 = 0

day 4:
f1 = 4
f2 = 8
total = 4 + 8 = 12
bonus = 12 / 13 = 0

Total bonus = 0

2. For every franchisee whose total sales across all days is a multiple of 13,
that multiple will be given as bonuses.

f1 = 1 + 2 + 3 + 4 = 10
bonus f1 = 10 / 13 = 0
f2 = 5 + 6 + 7 + 8 = 26
bonus f2 = 26 / 13 = 2

Total bonus = 2
"""
