"""
The function rotate_left_till_zero() takes an integer array containing one 0 
and rotates the array counterclockwise so that the 0 ends up at the front of 
the array.
"""
from collections import deque


def rotate_left_till_zero(array):
    my_deque = deque(array)
    while my_deque[0] != 0:
        my_deque.append(my_deque.popleft())
    return list(my_deque)