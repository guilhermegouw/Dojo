"""
You're a hacker (an ethical one, of course) who's trying to figure out
someone's password. You decide on a brute-force approach, and write some code
that produces every possible string of a given length.
"""

from itertools import product


def password_cracker(length: int) -> list:
    """
    In ASCII, the letter 'a' has the code 97, and 'z' has the code 122.
    """
    lowercase = [chr(i) for i in range(97, 123)]
    return list(product(lowercase, repeat=length))
