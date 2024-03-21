import pytest

from .challenge import is_palindrome


@pytest.mark.parametrize(
    "string,expected",
    [
        ("a", True),
        ("ab", False),
        ("aa", True),
        ("aba", True),
        ("abc", False),
        ("abccba", True),
    ],
)
def test_is_palindrome(string, expected):
    assert is_palindrome(string) == expected
