import pytest
from challenge import occupied_spaces_on_both_days


@pytest.mark.parametrize(
    ("n", "yesterday", "today", "expected"),
    [(1, "C", "C", 1), (1, ".", ".", 0), (2, "C.", ".C", 0)],
)
def test_occupied_spaces_on_both_days(n, yesterday, today, expected):
    assert occupied_spaces_on_both_days(n, yesterday, today) == expected
