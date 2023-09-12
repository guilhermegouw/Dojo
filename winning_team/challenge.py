"""
In basketball, three plays score points: a three-point shot, a two-point shot, and a one-point free throw.
You just watched a basketball game between the Apples and Bananas and recorded the number of successful 
three-point, two-point, and one-point plays for each team. 
Indicate whether 
the game was won by the Apples, 
the game was won by the Bananas, 
or the game was a tie.

Input
There are six lines of input. 
The ﬁrst three give the scoring for the Apples, 
and the latter three give the scoring for the Bananas.
The ﬁrst line gives the number of successful three-point shots for the Apples.
The second line gives the number of successful two-point shots for the Apples.
The third line gives the number of successful one-point free throws for the Apples.

The fourth line gives the number of successful three-point shots for the Bananas.
The ﬁfth line gives the number of successful two-point shots for the Bananas.
The sixth line gives the number of successful one-point free throws for the Bananas.
Each number is an integer between 0 and 100.

Output
The output is a single character.
If the Apples scored more points than the Bananas, output A (A for Apples).
If the Bananas scored more points than the Apples, output B (B for Bananas).
If the Apples and Bananas scored the same number of points, output T (T for Tie).
"""

def winning_team(three_apples, two_apples, one_apples, three_bananas, two_bananas, one_bananas):
    score_apples = 3*three_apples + 2*two_apples + one_apples
    score_bananas = 3*three_bananas + 2*two_bananas + one_bananas

    if score_apples > score_bananas:
        return "A"
    elif score_bananas > score_apples:
        return "B"
    else:
        return "T"


if __name__ == "__main__":
    three_apples = int(input())
    two_apples = int(input())
    one_apples = int(input())
    three_bananas = int(input())
    two_bananas = int(input())
    one_bananas = int(input())
    print(winning_team(three_apples, two_apples, one_apples, three_bananas, two_bananas, one_bananas))