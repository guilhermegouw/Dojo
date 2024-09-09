import pytest
from challenge import sort_king_names


@pytest.mark.parametrize(
    "kings, expected",
    [
        (
            [
                "Louis IX",
                "Louis VIII",
                "Henry IV",
                "Henry VIII",
                "Charles II",
                "Charles I",
            ],
            [
                "Charles I",
                "Charles II",
                "Henry IV",
                "Henry VIII",
                "Louis VIII",
                "Louis IX",
            ],
        ),
    ],
)
def test_sort_king_names(kings, expected):
    assert sort_king_names(kings) == expected
