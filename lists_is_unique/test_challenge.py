import pytest

from .challenge import is_unique_1, is_unique_2, is_unique_3


@pytest.mark.parametrize(
    "string,expected",
    [
        ("a", True),
        ("ab", True),
        ("aa", False),
        ("abc", True),
        ("aac", False),
        ("abcd", True),
        ("abcc", False),
    ],
)
def test_is_unique_1(string, expected):
    assert is_unique_1(string) == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("a", True),
        ("ab", True),
        ("aa", False),
        ("abc", True),
        ("aac", False),
        ("abcd", True),
        ("abcc", False),
    ],
)
def test_is_unique_2(string, expected):
    assert is_unique_2(string) == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("a", True),
        ("ab", True),
        ("aa", False),
        ("abc", True),
        ("aac", False),
        ("abcd", True),
        ("abcc", False),
    ],
)
def test_is_unique_3(string, expected):
    assert is_unique_3(string) == expected
