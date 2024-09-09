import pytest
from challenge import get_total_number_of_plays


@pytest.mark.parametrize(
    (
        "quarters",
        "first_machine_plays",
        "second_machine_plays",
        "third_machine_plays",
        "expected",
    ),
    [
        (1, 34, 0, 0, 40),  # Martha wins on first machine's first play
        (2, 0, 99, 0, 80),  # Martha wins on second machine's first play
        (3, 0, 0, 9, 12),  # Martha wins on third machine's first play
    ],
)
def test_get_total_number_of_plays(
    quarters,
    first_machine_plays,
    second_machine_plays,
    third_machine_plays,
    expected,
):
    assert (
        get_total_number_of_plays(
            quarters,
            first_machine_plays,
            second_machine_plays,
            third_machine_plays,
        )
        == expected
    )


"""
Exploring the problem:

    Plays until pay:
        - first: 35 -> 30 coins
        - second: 100 -> 60 coins
        - third: 10 -> 9 coins


Scenario 1:

Round 1:

quarters = 1
plays = 0
first_machine_plays = 34
second_machine_plays = 0
third_machine_plays = 0

quarters: 1 - 1 -> 0
first_machine_plays = 34 + 1 -> 35
    Prize! quarters + 30 -> (0 + 30 = 30)
    first_machine_plays = 0
quarters: 30 - 1 -> 29
second_machine_plays = 0 + 1 -> 1
quarters: 29 - 1 -> 28
third_machine_plays = 0 + 1 -> 1
plays = 0 + 1 -> 1

Observations:
Round costs: 3 quarters
Each round add one play to each machine.

Round 2:

quarters = 28
plays = 1
first_machine_plays = 0 -> Next Prize in 35 rounds
second_machine_plays = 1 -> Next Prize in 99 rounds
third_machine_plays = 1 -> Next Prize in 9 rounds
plays += 1 -> 2

Round 3:

quarters = 25
first_machine_plays = 1 -> Next Prize in 34 rounds
second_machine_plays = 2 -> Next Prize in 98 rounds
third_machine_plays = 2 -> Next Prize in 8 rounds

Round 4:

quarters = 22
first_machine_plays = 2 -> Next Prize in 33 rounds
second_machine_plays = 3 -> Next Prize in 97 rounds
third_machine_plays = 3 -> Next Prize in 7 rounds

Round 5:

quarters = 19
first_machine_plays = 3 -> Next Prize in 32 rounds
second_machine_plays = 4 -> Next Prize in 96 rounds
third_machine_plays = 4 -> Next Prize in 6 rounds

Round 6:

quarters = 16
first_machine_plays = 4 -> Next Prize in 31 rounds
second_machine_plays = 5 -> Next Prize in 95 rounds
third_machine_plays = 5 -> Next Prize in 5 rounds

Round 7:

quarters = 13
first_machine_plays = 5 -> Next Prize in 30 rounds
second_machine_plays = 6 -> Next Prize in 94 rounds
third_machine_plays = 6 -> Next Prize in 4 rounds

Round 8:

quarters = 10
first_machine_plays = 6 -> Next Prize in 29 rounds
second_machine_plays = 7 -> Next Prize in 93 rounds
third_machine_plays = 7 -> Next Prize in 3 rounds

Round 9:

quarters = 7
first_machine_plays = 7 -> Next Prize in 28 rounds
second_machine_plays = 8 -> Next Prize in 92 rounds
third_machine_plays = 8 -> Next Prize in 2 rounds

Round 10:

quarters = 4
first_machine_plays = 8 -> Next Prize in 27 rounds
second_machine_plays = 9 -> Next Prize in 91 rounds
third_machine_plays = 9 -> Next Prize in 1 rounds

Round 11:

quarters = 1
first_machine_plays = 9 -> Next Prize in 26 rounds
second_machine_plays = 10 -> Next Prize in 90 rounds
third_machine_plays = 10 -> Next Prize in 0 rounds
    Prize! quarters + 9 (1 + 9) -> 10
    third_machine_plays = 0

Round 12:

quarters = 10 - 2 = 7
first_machine_plays = 10 -> Next Prize in 25 rounds
second_machine_plays = 9 -> Next Prize in 89 rounds
third_machine_plays = 1 -> Next Prize in 9 rounds

No more Prizes to come, so Martha will only play the remaining coins until she loses...
"""
