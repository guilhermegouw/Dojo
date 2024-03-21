"""
This function accepts an array of arrays, where the inner arrays
contain 1's and 0's. The function then returns how many 1's there are.
So, for this example input:
[
[0, 1, 1, 1, 0],
[0, 1, 0, 1, 0, 1],
[1, 0]
]
our function will return 7, since there are seven 1's.
"""


def count_ones(arr):
    return sum(item.count(1) for item in arr)