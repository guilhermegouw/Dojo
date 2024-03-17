import pytest
from challenge import can_organize


@pytest.mark.parametrize(
    "boxes,contents,expected",
    [
        (2, ((2, 1, 2), (2, 3, 4)), "YES"),
        (2, ((2, 1, 3), (2, 2, 4)), "NO"),
        (3, ((2, 1, 2), (2, 3, 4), (1, 5)), "YES"),
        (3, ((2, 1, 2), (2, 3, 6), (1, 5)), "NO"),
    ],
)
def test_can_organize(boxes, contents, expected):
    assert can_organize(boxes, *contents) == expected
