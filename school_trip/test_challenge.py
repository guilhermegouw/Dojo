import pytest
from challenge import need_to_raise_more_money


@pytest.mark.parametrize(
    "cost, proportions, n, expected",
    [
        (50, [0.25, 0.25, 0.25, 0.25], 4, "YES"),
    ],
)
def test_need_to_raise_more_money(cost, proportions, n, expected):
    assert need_to_raise_more_money(cost, proportions, n) == expected


"""
EXPLORE THE CHALLENGE

CASE 1:
money_needed = 50 * 2 = 100
first_year = 0.25 * 4 = 1 -> 1 * 12 = 12
second_year = 0.25 * 4 = 1 -> 1 * 10 = 10
third_year = 0.25 * 4 = 1 -> 1 * 7 = 7
fourth_year = 0.25 * 4 = 1 -> 1 * 5 = 5
total_raised = 12 + 10 + 7 + 5 = 34

money_needed > total_raised -> YES
"""
