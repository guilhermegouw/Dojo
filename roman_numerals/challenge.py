"""
Roman Numeral to Integer Converter

Objective:

Write a function that takes a Roman numeral as input and converts it into an
integer.

Background:

Roman numerals are represented by combinations of letters from the Latin
alphabet: I, V, X, L, C, D, and M.
Each letter corresponds to a specific value:

• I = 1
• V = 5
• X = 10
• L = 50
• C = 100
• D = 500
• M = 1000

Roman numerals are usually written from largest to smallest, from left to
right.
However, there are exceptions to this rule.
For instance
 - IV represents 4 (one less than 5)
 - and IX represents 9 (one less than 10).
These are called subtractive combinations.

Rules for Roman Numerals:

1. If a smaller numeral appears before a larger one, subtract the smaller
value from the larger one.
  •  Example: IV = 4 (5 - 1), IX = 9 (10 - 1)
2. If the numeral appears in a descending order (or equal), add the values.
  •  Example: VI = 6 (5 + 1), MCMXC = 1990 (1000 + 900 + 90)

Function Signature:
Your task is to implement a function roman_to_int(s: str) -> int where:

  • Input: A string roman representing a valid Roman numeral.
  • Output: An integer representing the corresponding Roman numeral.
"""


def convert_roman_to_int(roman: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    integer = roman_dict[roman[0]]
    for i in range(1, len(roman)):
        integer += roman_dict[roman[i]]
        if roman_dict[roman[i]] > roman_dict[roman[i - 1]]:
            integer -= roman_dict[roman[i - 1]] * 2
    return integer


if __name__ == "__main__":
    convert_roman_to_int("IV")
