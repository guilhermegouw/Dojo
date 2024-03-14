"""
Finding the mode:
In statistics, the mode of a set of values is the value that appears most often.
Write code that processes an array of survey data, where survey takers have
responded to a question with a number in range 1-10, to determine the mode of 
the data set. For our purpose, if multiple modes exist, return any of them.
"""


def get_mode(seq):
    """Return mode of a sequence."""
    frequencies = {}
    for value in seq:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1
    for k, v in frequencies.items():
        if v == max(frequencies.values()):
            return k


def get_mode_pythonic(seq):
    """
    Return mode of a sequence using Pythonic way.

    """
    return max(set(seq), key=seq.count)
