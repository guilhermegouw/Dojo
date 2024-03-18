import pytest

from .challenge import word_builder, book_word_builder, word_builder_3_chars


@pytest.mark.parametrize(
    "array,expected",
    [
        (
            ["a", "b"],
            [
                "ab",
                "ba",
            ],
        ),
        (["a", "b", "c"], ["ab", "ac", "ba", "bc", "ca", "cb"]),
        (
            ["a", "b", "c", "d"],
            [
                "ab",
                "ac",
                "ad",
                "ba",
                "bc",
                "bd",
                "ca",
                "cb",
                "cd",
                "da",
                "db",
                "dc",
            ],
        ),
        (
            ["a", "b", "c", "d", "e"],
            [
                "ab",
                "ac",
                "ad",
                "ae",
                "ba",
                "bc",
                "bd",
                "be",
                "ca",
                "cb",
                "cd",
                "ce",
                "da",
                "db",
                "dc",
                "de",
                "ea",
                "eb",
                "ec",
                "ed",
            ],
        ),
    ],
)
def test_word_builder(array, expected):
    assert word_builder(array) == expected


@pytest.mark.parametrize(
    "array,expected",
    [
        (
            ["a", "b"],
            [
                "ab",
                "ba",
            ],
        ),
        (["a", "b", "c"], ["ab", "ac", "ba", "bc", "ca", "cb"]),
        (
            ["a", "b", "c", "d"],
            [
                "ab",
                "ac",
                "ad",
                "ba",
                "bc",
                "bd",
                "ca",
                "cb",
                "cd",
                "da",
                "db",
                "dc",
            ],
        ),
        (
            ["a", "b", "c", "d", "e"],
            [
                "ab",
                "ac",
                "ad",
                "ae",
                "ba",
                "bc",
                "bd",
                "be",
                "ca",
                "cb",
                "cd",
                "ce",
                "da",
                "db",
                "dc",
                "de",
                "ea",
                "eb",
                "ec",
                "ed",
            ],
        ),
    ],
)
def test_book_word_builder(array, expected):
    assert book_word_builder(array) == expected


@pytest.mark.parametrize(
    "array,expected",
    [
        (
            ["a", "b", "c"],
            ["abc", "acb", "bac", "bca", "cab", "cba"],
        )
    ],
)
def test_word_builder_3_chars(array, expected):
    assert word_builder_3_chars(array) == expected
