import pytest
from think_like_a_programmer.ch_03.mode import get_mode


@pytest.mark.parametrize(
    "seq, expected",
    [
        ([1, 2, 3, 4, 10, 6, 7, 8, 9, 10], 10),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1),
        ([1, 2, 3, 4, 5], 1),
    ],
)
def test_get_mode(seq, expected):
    assert get_mode(seq) == expected
