import pytest
from challenge import get_smallest_neighborhood


@pytest.mark.parametrize(
    "villages, expected",
    [
        ([6, 10, 15], 4.5),
        ([6, 10, 15, 18], 4),
    ],
)
def test_get_smallest_neighborhood(villages, expected):
    assert get_smallest_neighborhood(villages) == expected
