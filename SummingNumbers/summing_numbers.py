"""
Write a my_sum function that takes a sequence of numbers and returns the sum of the numbers.
my_sum should be able to receive a flexible number of arguments.
The arguments can be either be a list of numbers or several numbers as individual arguments.
"""


def my_sum(*args):
    total = 0
    for arg in args:
        if hasattr(arg, "__iter__"):
            total += my_sum(*arg)
        else:
            total += arg
    return total
