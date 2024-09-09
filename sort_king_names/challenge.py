"""
Sorting Kings Names

Objective:

You are given a list of king names where each king’s name is followed by a
Roman numeral (e.g., “Louis XIV”, “Henry VIII”).
Your task is to write a function that sorts the list of kings,
first by their name and then by the numeric value of their Roman numeral.

Details:

Each entry in the dataset contains:

1. A king’s name (a string containing only alphabetic characters and spaces).
2. A Roman numeral (representing a number between 1 and 1000).

You must sort the kings:

• Alphabetically by the king’s name.
• Numerically by the value of the Roman numeral for entries with the same name.

Roman Numeral Values:

• I = 1, II = 2, III = 3, IV = 4, V = 5
• VI = 6, VII = 7, VIII = 8, IX = 9, X = 10
• L = 50, C = 100, D = 500, M = 1000

Function Signature:

• Input: A list of strings names, where each string contains a king’s name
followed by a Roman numeral.
    Sample: [
                "Louis IX", "Louis VIII",
                "Henry IV", "Henry VIII",
                "Charles II", "Charles I"
            ]

• Output: A list of strings sorted by name, and by the value of the Roman
numeral.
    Sample: [
                'Charles I', 'Charles II',
                'Henry IV', 'Henry VIII',
                'Louis VIII', 'Louis IX'
            ]
"""


def sort_king_names(kings):
    dict_names = {}
    for king in kings:
        name, numeral = king.split()
        dict_names[f"{name} {convert_roman_to_int(numeral)}"] = king
    sorted_dict_names = dict(sorted(dict_names.items()))

    return list(sorted_dict_names.values())


def convert_roman_to_int(roman):
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
    sort_king_names(
        [
            "Louis IX",
            "Louis VIII",
            "Henry IV",
            "Henry VIII",
            "Charles II",
            "Charles I",
        ]
    )
