"""
The Challenge

Two players, A and B, are playing a card game.
The game starts with a deck of 52 cards. 
- Player A takes a card from the deck, then player B takes a card from the deck, 
then player A, then player B, until  there are no cards left in the deck.
- There are 13 types of cards in the deck. 
These types are as follows: 
two, three, four, ﬁve, six, seven, eight, nine, ten, jack, queen, king, ace. 
There are four cards of each of these types in the deck. 
For example: 
there are four twos, four threes, and so on, all the way up to four aces. 
(That's why there are 52 cards in the deck: 13 types times 4 cards per type.)
A high card is a card that is a jack, queen, king, or ace.
When a player takes a high card, they may score some points.

Here are the rules by which points are scored:

- If a player takes a jack, after which there is at least one card remaining in 
the deck, and the next card in the deck is not a high card, then the player 
scores 1 point.
- If a player takes a queen, after which there are at least two cards remaining 
in the deck, and neither of the next two cards in the deck is a high card, 
then the player scores 2 points.
- If a player takes a king, after which there are at least three cards remaining 
in the deck, and none of the next three cards in the deck is a high card, then 
the player scores 3 points.
- If a player takes an ace, after which there are at least four cards remaining 
in the deck, and none of the next four cards in the deck is a high card, then 
the player scores 4 points.
We're asked to output information each time a player scores, as well as the total 
score for each player at the end of the game.

Input

The input consists of 52 lines. 
Each line contains the type of a card in the deck. 
The lines are in the order that cards will be taken from the deck; that is, the 
ﬁrst line is the ﬁrst card taken from the deck, the second line is the second 
card taken, and so on.

Output

Whenever a player scores, output the following line:
Player p scores q point(s).
where p is A for player A or B for player B, and q is the number of points that they 
just scored.
When the game ends, output the following two lines:
Player A: m point(s).
Player B: n point(s).
where m is the total score for player A and n is the total score for player B.
"""

def get_scores(deck):
    high_cards = ['jack', 'queen', 'king', 'ace']
    a_score = 0
    b_score = 0
    i = 0
    for card in deck:
        if (card == 'jack' 
            and len(deck) - i > 1 
            and deck[i + 1] not in high_cards):
            if i % 2 == 0:
                a_score += 1
            else:
                b_score += 1
        elif (card == 'queen' 
              and len(deck) - i > 2
              and deck[i + 1] not in high_cards
              and deck[i + 2] not in high_cards):
            if i % 2 == 0:
                a_score += 2
            else:
                b_score += 2
        elif (card == 'king' 
              and len(deck) - i > 3
              and deck[i + 1] not in high_cards
              and deck[i + 2] not in high_cards
              and deck[i + 3] not in high_cards
              ):
            if i % 2 == 0:
                a_score += 3
            else:
                b_score += 3
        elif (card == 'ace' 
              and len(deck) - i > 4
              and deck[i + 1] not in high_cards
              and deck[i + 2] not in high_cards
              and deck[i + 3] not in high_cards
              and deck[i + 4] not in high_cards
              ):
            if i % 2 == 0:
                a_score += 4
            else:
                b_score += 4
        i += 1
    return a_score, b_score
