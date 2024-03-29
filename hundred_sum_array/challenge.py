"""
The function returns true if the array is a “100-Sum Array,” and false if it 
is not.

A “100-Sum Array” meets the following criteria:

• Its first and last numbers add up to 100.
• Its second and second-to-last numbers add up to 100.
• Its third and third-to-last numbers add up to 100, and so on.
"""


def one_hundred_sum(array):
    left = 0
    right = len(array) - 1
    for i in range(0, len(array) // 2):
        if array[left] + array[right] != 100:
            return False
        left += 1
        right -= 1
    return True
