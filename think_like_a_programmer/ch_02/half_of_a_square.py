"""
Write a program with only outputs
That prints the half of a square using "#" characters
"""


def half_of_a_square():
    for i in range(5, 0, -1):
        print("#" * i)


def full_square():
    for i in range(5):
        print("#" * 5)


def sideways_triangle():
    for i in range(5):
        print("#" * (i + 1))

    for i in range(4, 0, -1):
        print("#" * i)


half_of_a_square()
full_square()
sideways_triangle()