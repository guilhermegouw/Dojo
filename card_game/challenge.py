"""
The Challenge

Two players, A and B, are playing a card game.
- The game starts with a deck of 52 cards.
- Player A takes a card from the deck, then player B takes a card from the
  deck, then player A, then player B, until there are no cards left.
- There are 13 types of cards in the deck. These types are as follows:
  two, three, four, ﬁve, six, seven, eight, nine, ten, jack, queen, king,
  ace. There are four cards of each of these types in the deck.

For example:
- There are four twos, four threes, and so on, all the way up to four aces.
- A high card is a card that is a jack, queen, king, or ace.
- When a player takes a high card, they may score some
  points. Here are the rules by which points are scored:
    - If a player takes a jack, after which there is at least one card
      remaining in the deck, and the next card in the deck is not a high card,
      then the player scores 1 point.
    - If a player takes a queen, after which there are at least two cards
      remaining in the deck, and neither of the next two cards in the deck is
      a high card, then the player scores 2 points.
    - If a player takes a king, after which there are at least three cards
      remaining in the deck, and none of the next three cards in the deck is a
      high card, then the player scores 3 points.
    - If a player takes an ace, after which there are at least four cards
      remaining in the deck, and none of the next four cards in the deck is a
      high card, then the player scores 4 points.

We’re asked to output information each time a player scores, as well as the
total score for each player at the end of the game.

Input

The input consists of 52 lines. Each line contains the type of a card in the
deck. The lines are in the order that cards will be taken from the deck;
that is, the ﬁrst line is the ﬁrst card taken from the deck, the second
line is the second card taken, and so on.

Output

a dict with keys A and B, each containing the total score for that player.
"""

from itertools import cycle


def get_score(deck):
    score = {"A": 0, "B": 0}
    high_cards = ["jack", "queen", "king", "ace"]
    player = cycle(["A", "B"])

    for i, card in enumerate(deck):
        current_player = next(player)

        score_rules = {
            "jack": {
                "high_cards": all(
                    deck[j] not in high_cards
                    for j in range(i + 1, min(i + 2, len(deck)))
                ),
                "points": 1,
            },
            "queen": {
                "high_cards": all(
                    deck[j] not in high_cards
                    for j in range(i + 1, min(i + 3, len(deck)))
                ),
                "points": 2,
            },
            "king": {
                "high_cards": all(
                    deck[j] not in high_cards
                    for j in range(i + 1, min(i + 4, len(deck)))
                ),
                "points": 3,
            },
            "ace": {
                "high_cards": all(
                    deck[j] not in high_cards
                    for j in range(i + 1, min(i + 5, len(deck)))
                ),
                "points": 4,
            },
        }

        if card in score_rules and score_rules[card]["high_cards"]:
            score[current_player] += score_rules[card]["points"]
    return score


if __name__ == "__main__":
    deck = [
        "10",
        "jack",
        "2",
    ]
    score = get_score(deck)
    print(score)
