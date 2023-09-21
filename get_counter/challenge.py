"""
get_counter() takes an integer array and returns a hash table with the array 
elements as keys and their frequencies as values.
"""


def get_counter(array):
    counter = {}
    for num in array:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    return counter
