"""
array = [1, 2, 3, 4]
sequence = [1, 3, 4]

1 in [1, 2, 3, 4] -> True and idx = 0
                  -> array_second = [2, 3, 4]
                  -> array = [idx + 1:]
3 in [2, 3, 4] -> True and idx = 2
               -> array_third = [4]
               -> array = [idx + 1:]
"""


def is_valid_subsequence(array, sequence):
    item_idx = 0
    for item in sequence:
        if item in array[item_idx:]:
            item_idx = array.index(item) + 1
        else:
            return False
    return True
