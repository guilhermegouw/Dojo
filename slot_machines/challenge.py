"""
The Challenge

Martha goes to a casino and brings n quarters.
The casino has three slot machines, and she plays them in order until she has
no quarters left.
That is, she plays the first slot machine, then the second, then the third,
then back to the first, then the second, and so on.
Each play costs one quarter.

The slot machines operate according to the following rules:

- The first slot machine pays 30 quarters every 35th time it is played.
- The second slot machine pays 60 quarters every 100th time it is played.
- The third slot machine pays 9 quarters every 10th time it is played.
No other plays pay anything.

Determine the number of times Martha plays before she has no quarters left.

Input

The input consists of four lines.
- The first line contains an integer n, the number of quarters that Martha
  brings to the casino.
- The second line contains an integer indicating the number of times that the
  first slot machine has been played since it last paid.
  These plays occurred prior to Martha arriving, and Martha’s plays continue
  from there.

For example:

Suppose that the first slot machine has been played 34 times since it last paid
Then, Martha will win 30 quarters the first time she plays it.
- The third line contains an integer indicating the number of times that the
second slot machine has been played since it last paid.
- The fourth line contains an integer indicating the number of times that the
third slot machine has been played since it last paid.

Output

Output the following sentence, where x is the number of times Martha plays
before she has no quarters left
"""

# def get_total_number_of_plays(
#     quarters, first_machine_plays, second_machine_plays, third_machine_plays
# ):
#     plays = 0
#     machine = 1
#     while quarters > 0:
#         if machine == 1:
#             quarters -= 1
#             first_machine_plays += 1
#             plays += 1
#             machine = 2
#             if first_machine_plays == 35:
#                 quarters += 30
#                 first_machine_plays = 0
#         elif machine == 2:
#             quarters -= 1
#             second_machine_plays += 1
#             plays += 1
#             machine = 3
#             if second_machine_plays == 100:
#                 quarters += 60
#                 second_machine_plays = 0
#         elif machine == 3:
#             quarters -= 1
#             third_machine_plays += 1
#             plays += 1
#             machine = 1
#             if third_machine_plays == 10:
#                 quarters += 9
#                 third_machine_plays = 0
#     return plays


def get_total_number_of_plays(
    quarters, first_machine_plays, second_machine_plays, third_machine_plays
):
    plays = 0
    machines = [
        {
            "plays_needed": 35,
            "reward": 30,
            "current_plays": first_machine_plays,
        },
        {
            "plays_needed": 100,
            "reward": 60,
            "current_plays": second_machine_plays,
        },
        {
            "plays_needed": 10,
            "reward": 9,
            "current_plays": third_machine_plays,
        },
    ]
    machine_index = 0

    while quarters > 0:
        quarters -= 1
        machines[machine_index]["current_plays"] += 1
        plays += 1

        if (
            machines[machine_index]["current_plays"]
            == machines[machine_index]["plays_needed"]
        ):
            quarters += machines[machine_index]["reward"]
            machines[machine_index]["current_plays"] = 0

        machine_index = (machine_index + 1) % 3

    return plays
