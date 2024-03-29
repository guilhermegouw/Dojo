import pytest

from .challenge import one_hundred_sum


@pytest.mark.parametrize(
    "array,expected",
    [
        ([49, 51], True),
        ([50, 51], False),
        ([48, 49, 51, 52], True),
        ([48, 49, 50, 52], False),
        ([48, 49, 50, 51, 52], True),
        ([97, 60, 50, 48, 49, 50, 51, 52, 50, 40, 3], True),
        ([97, 60, 50, 48, 49, 50, 52, 52, 50, 40, 3], False),
    ],
)
def test_one_hundred_sum(array, expected):
    assert one_hundred_sum(array) == expected
