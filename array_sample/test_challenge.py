import pytest
from .challenge import sample


@pytest.mark.parametrize(
    "array,expected",
    [
        ([1, 2, 3], (1, 2, 3)),
        ([1, 2, 3, 4, 5, 6], (1, 4, 6)),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (1, 6, 10)),
    ],
)
def test_sample(array, expected):
    assert sample(array) == expected
