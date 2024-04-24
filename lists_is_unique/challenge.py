"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique_1(string):
    return len(string) == len(set(string))


def is_unique_2(string):
    checked_chars = []
    for char in string:
        if char not in checked_chars:
            checked_chars.append(char)
        else:
            return False
    return True


def is_unique_3(string):
    sorted_string = sorted(string)
    for i in range(len(string) -1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False
    return True
