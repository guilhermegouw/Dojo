"""
In this problem, we’ll assume that phone numbers are four digits. 
A phone number belongs to a telemarketer if its four digits satisfy 
all three of the following properties:

- The ﬁrst digit is 8 or 9.
- The fourth digit is 8 or 9.
- The second and third digits are the same.

For example, a phone number whose four digits are 8119 belongs to a telemarketer.

Determine whether a phone number belongs to a telemarketer, and indicate whether 
we should answer the phone or ignore it.


Input
There are four lines of input. 
These lines give the ﬁrst, second, third, and fourth digits of the phone number, respectively. 
Each digit is an integer between 0 and 9.

Output
- If the phone number belongs to a telemarketer, output ignore;
- otherwise, output answer.
"""


def is_telemarketer(first, second, third, fourth):
    telemarketer = (
        first in ['8', '9'] 
        and second == third
        and fourth in ['8', '9']        
    )

    if telemarketer:
        return 'ignore'
    else:
        return 'answer'


if __name__=='__main__':
    first = input()
    second = input()
    third = input()
    fourth = input()

    print(is_telemarketer(first, second, third, fourth))
