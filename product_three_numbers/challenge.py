"""
This function finds the greatest product of three numbers from a given array:
"""


def largest_product(array):
    sorted_array = sorted(array)
    return sorted_array[-1] * sorted_array[-2] * sorted_array[-3]
