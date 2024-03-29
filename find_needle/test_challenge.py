import pytest

from .challenge import find_needle, find_needle_2


@pytest.mark.parametrize(
    "needle,haystack,expected",
    [
        ("def", "abcdefghi", True),
        ("dd", "abcdefghi", False),
        ("def", "def", True),
        ("def", "ddf", False),
        ("def", "defg", True),
        ("def", "ddfg", False),
        ("def", "abcdedefgh", True),
        ("df", "abcdedefgh", False),
    ],
)
def test_find_needle(needle, haystack, expected):
    assert find_needle(needle, haystack) == expected


@pytest.mark.parametrize(
    "needle,haystack,expected",
    [
        ("def", "abcdefghi", True),
        ("dd", "abcdefghi", False),
        ("def", "def", True),
        ("def", "ddf", False),
        ("def", "defg", True),
        ("def", "ddfg", False),
        ("def", "abcdedefgh", True),
        ("df", "abcdedefgh", False),
    ],
)
def test_find_needle_2(needle, haystack, expected):
    assert find_needle_2(needle, haystack) == expected
