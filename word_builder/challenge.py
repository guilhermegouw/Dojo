"""
Write algorithm that collects every combination of two-character strings built
from an array of single characters.
For example, given the array: ["a", "b", "c", "d"], we'd return a new array
containing the following string combinations:
[
'ab', 'ac', 'ad', 'ba', 'bc', 'bd',
'ca', 'cb', 'cd', 'da', 'db', 'dc'
]
"""

import time


def word_builder(array):
    words = []
    for i in range(len(array)):
        new = [item for item in array if item != array[i]]
        [words.append(array[i] + item) for item in new]
    return words


def book_word_builder(array):
    collection = []
    for i in range(len(array)):
        j = 0
        for j in range(j, len(array)):
            if i != j:
                collection.append(array[i] + array[j])
    return collection


if __name__ == "__main__":
    array = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    start = time.time()
    word_builder(array)
    print(time.time() - start)
    start = time.time()
    book_word_builder(array)
    print(time.time() - start)
