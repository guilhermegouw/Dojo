"""
Create a function that takes a small sample of an array.
We expect to have very large arrays, so our sample is just the first,
middlemost, and last value from the array.

Example:

array = [1, 2, 3]
first = 1
middle = 2
last = 3


array = [1, 2, 3, 4, 5, 6]
first = 1
middle = 4
last = 6
"""


def sample(array):
    first = array[0]
    middle = array[int(len(array) / 2)]
    last = array[len(array) - 1]
    return first, middle, last
