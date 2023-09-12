"""
The Challenge

Martha goes to a casino and brings n quarters. The casino has three slot 
machines, and she plays them in order until she has no quarters left. 
That is, she plays the ﬁrst slot machine, then the second, then the third, 
then back to the ﬁrst, then the second, and so on. 
Each play costs one quarter.

The slot machines operate according to the following rules:
- The ﬁrst slot machine pays 30 quarters every 35th time it is played.
- The second slot machine pays 60 quarters every 100th time it is played.
- The third slot machine pays 9 quarters every 10th time it is played.
- No other plays pay anything.

Determine the number of times Martha plays before she has no quarters left.

Input

The input consists of four lines.
- The ﬁrst line contains an integer n, the number of quarters that Martha brings 
to the casino. n is between 1 and 1,000.
- The second line contains an integer indicating the number of times that the 
ﬁrst slot machine has been played since it last paid. These plays occurred prior 
to Martha arriving, and Martha's plays continue from there.
For example: 
- Suppose that the ﬁrst slot machine has been played 34 times since it last paid. 
Then, Martha will win 30 quarters the ﬁrst time she plays it.
- The third line contains an integer indicating the number of times that the second 
slot machine has been played since it last paid.
- The fourth line contains an integer indicating the number of times that the third 
slot machine has been played since it last paid.

Output

Output the following sentence, where x is the number of times Martha plays before she 
has no quarters left:

Martha plays x times before going broke.
"""

def get_plays_before_broke(initial_quarters, first_plays, second_plays, third_plays):
    first_machine_limit = 35
    second_machine_limit = 100
    third_machine_limit = 10

    first_machine_prize = 30
    second_machine_prize = 60
    third_machine_prize = 9
    
    martha_plays = 0
    martha_quarters = initial_quarters
    machine_of_the_turn = 1
    first_machine_plays = first_plays
    second_machine_plays = second_plays
    third_machine_plays = third_plays

    while martha_quarters > 0:
        martha_plays += 1
        martha_quarters -= 1

        if machine_of_the_turn == 1:
            first_machine_plays += 1
            machine_of_the_turn = 2
            if first_machine_plays == first_machine_limit:
                martha_quarters += first_machine_prize
                first_machine_plays = 0

        elif machine_of_the_turn == 2:
            second_machine_plays += 1
            machine_of_the_turn = 3
            if second_machine_plays == second_machine_limit:
                martha_quarters += second_machine_prize
                second_machine_plays = 0

        elif machine_of_the_turn == 3:
            third_machine_plays += 1
            machine_of_the_turn = 1
            if third_machine_plays == third_machine_limit:
                martha_quarters += third_machine_prize
                third_machine_plays = 0
    
    return f"Martha plays {martha_plays} times before going broke."


if __name__=="__main__":
    print(get_plays_before_broke(7, 28, 0, 8))