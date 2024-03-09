"""

"""


def isValidSubsequence(array, sequence):
    for item in sequence:
        if item in array:
            array = array[array.index(item) + 1:]
        else:
            return False
    return True
