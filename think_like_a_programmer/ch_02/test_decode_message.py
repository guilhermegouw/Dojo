import pytest

import think_like_a_programmer.ch_02.decode_a_message as dm


@pytest.mark.parametrize(
    "input, expected",
    [
        ("18", "R"),
        ("241", "Y"),
    ],
)
def test_decode_upper_mode(input, expected):
    assert dm.decode_upper_mode(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("171", "i"),
        ("763", "g"),
        ("98423", "h"),
        ("1208", "t"),
        ('32', 'e'),
        ('20620', 's'),
    ],
)
def test_decode_lower_mode(input, expected):
    assert dm.decode_lower_mode(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("11", "?"),
        ("500", " "),
        ('10', '!'),
    ],
)
def test_decode_punctuation_mode(input, expected):
    assert dm.decode_punctuation_mode(input) == expected


def test_decode_a_message():
    assert dm.decode_message(
        "18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10"
        ) == "Right? Yes!"
