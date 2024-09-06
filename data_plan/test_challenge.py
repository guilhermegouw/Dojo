import pytest
from challenge import get_mb_available


@pytest.mark.parametrize(
    ("x", "n", "mb_used", "expected"),
    [
        (10, 1, [0], 20),
        (10, 1, [5], 15),
        (10, 2, [5, 5], 20),
        (10, 2, [0, 0], 30),
    ],
)
def test_get_mb_available(x, n, mb_used, expected):
    assert get_mb_available(x, n, mb_used) == expected
