"""
Exploring the challenge:

Scores are calculated based on the following rules:
- If a player takes a jack, after which there is at least one card remaining in
in the deck, and the next card in the deck is not a high card, then the player
scores 1 point.
- If a player takes a queen, after which there are at least two cards remaining
  in the deck, and neither of the next two cards in the deck is a high card,
  then the player scores 2 points.
- If a player takes a king, after which there are at least three cards
  remaining in the deck, and none of the next three cards in the deck is a high
  card, then the player scores 3 points.
- If a player takes an ace, after which there are at least four cards remaining
  in the deck, and none of the next four cards in the deck is a high card, then
  the player scores 4 points.
"""

import pytest
from challenge import get_score


@pytest.mark.parametrize(
    "deck, expected",
    [
        (["jack", "2"], {"A": 1, "B": 0}),
        (
            ["queen", "2", "3"],
            {"A": 2, "B": 0},
        ),
        (
            ["king", "2", "3", "4"],
            {"A": 3, "B": 0},
        ),
        (
            ["ace", "2", "3", "4", "5"],
            {"A": 4, "B": 0},
        ),
        (["10", "jack", "2"], {"A": 0, "B": 1}),
        (
            ["10", "queen", "2", "3"],
            {"A": 0, "B": 2},
        ),
        (
            ["10", "king", "2", "3", "4"],
            {"A": 0, "B": 3},
        ),
        (
            ["10", "ace", "2", "3", "4", "5"],
            {"A": 0, "B": 4},
        ),
    ],
)
def test_get_score(deck, expected):
    assert get_score(deck) == expected
