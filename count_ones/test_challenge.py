import pytest

from .challenge import count_ones


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([[0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0]], 7),
        ([[0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0], [1, 1, 1, 1]], 11),
        (
            [
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0, 1],
                [1, 0],
                [1, 1, 1, 1],
                [1, 1],
            ],
            13,
        ),
    ],
)
def test_count_ones(arr, expected):
    assert count_ones(arr) == expected
