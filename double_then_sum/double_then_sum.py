from typing import List


def double_then_sum(input_list: List[int]) -> int:
    """Return the sum of the elements of input_list doubled."""
    return sum(x * 2 for x in input_list)
