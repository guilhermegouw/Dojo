import pytest
from challenge import convert_roman_to_int


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("VI", 6),
        ("XI", 11),
        ("XV", 15),
    ],
)
def test_roman_to_int(roman, expected):
    assert convert_roman_to_int(roman) == expected
