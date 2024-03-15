import pytest
from double_then_sum import double_then_sum as ds


@pytest.mark.parametrize(
    "input,expected",
    [
        ([1], 2),
        ([3, 1], 8),
        ([1, 2, 3], 12),
        ([1, 2, 3, 4], 20),
    ],
)
def test_double_then_sum(input, expected):
    assert ds.double_then_sum(input) == expected
