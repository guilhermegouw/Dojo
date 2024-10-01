import pytest
from challenge import can_organize


@pytest.mark.parametrize(
    "boxes, expected",
    [
        ([[1, 2, 3], [5, 7], [2, 4]], "NO"),
        ([[4, 5, 7], [1, 2]], "YES"),
        ([[4, 5, 7], [6, 8]], "NO"),
        ([[1], [2], [3]], "YES"),
        ([[1, 2, 3], [4, 5, 6]], "YES"),
        ([[1, 3, 5], [2, 4, 6]], "NO"),
        ([[1, 2, 3], [3, 4, 5], [5, 6, 7]], "YES"),
        ([[1, 2, 3], [2, 3, 4], [1, 2, 3]], "NO"),
    ],
)
def test_can_organize(boxes, expected):
    assert can_organize(boxes) == expected
