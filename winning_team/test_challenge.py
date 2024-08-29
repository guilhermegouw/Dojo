import pytest
from challenge import get_winner


@pytest.mark.parametrize(
    "apples,bananas,winner",
    [
        ((1, 1, 1), (1, 1, 1), "T"),
        ((1, 1, 1), (0, 0, 0), "A"),
        ((0, 0, 0), (1, 1, 1), "B"),
        ((1, 1, 1), (1, 1, 0), "A"),
        ((1, 1, 0), (1, 1, 1), "B"),
    ],
)
def test_winner_no_points(apples, bananas, winner):
    assert get_winner(apples, bananas) == winner
