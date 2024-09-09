import pytest
from challenge import get_playlist


@pytest.mark.parametrize(
    "presses, expected",
    [
        ([(4, 1)], "A B C D E"),
        ([(1, 1), (4, 1)], "B C D E A"),
        ([(2, 1), (4, 1)], "E A B C D"),
        ([(3, 1), (4, 1)], "B A C D E"),
        (
            [(1, 1), (2, 1), (3, 1), (4, 1)],
            "B A C D E",
        ),
        (
            [(1, 2), (2, 2), (3, 2), (4, 2)],
            "A B C D E",
        ),
    ],
)
def test_get_playlist(presses, expected):
    assert get_playlist(presses) == expected
