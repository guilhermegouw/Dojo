"""
The Challenge

In this problem, we’ll assume that phone numbers are four digits. 
A phone number belongs to a telemarketer if its four digits satisfy all three
of the following properties:

The first digit is 8 or 9.
The fourth digit is 8 or 9.
The second and third digits are the same.

For example:
A phone number whose four digits are 8119 belongs to a telemarketer.

Determine whether a phone number belongs to a telemarketer, and indicate
whether we should answer the phone or ignore it.

Input

There are four lines of input. These lines give the ﬁrst, second, third, and
fourth digits of the phone number, respectively
Each digit is an integer between 0 and 9.

Output

If the phone number belongs to a telemarketer, output ignore;
otherwise, output answer.
"""


def is_telemarketer(phone_number):
    if (
        phone_number[0] in (8, 9)
        and phone_number[3] in (8, 9)
        and phone_number[1] == phone_number[2]
    ):
        answer = "ignore"
    else:
        answer = "answer"
    return answer
