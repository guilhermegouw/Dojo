import pytest

from think_like_a_programmer.ch_02.luhn_checksum_validation import should_double, get_doubled_values, luhn_checksum_validation


@pytest.mark.parametrize(
    "id_num, current_index, result",
    [
        ("1762483", 0, False),
        ("1762483", 1, True),
        ("1762483", 2, False),
        ("1762483", 3, True),
        ("1762483", 4, False),
        ("1762483", 5, True),
        ("123456", 0, True),
        ("123456", 1, False),
        ("123456", 2, True),
        ("123456", 3, False),
        ("123456", 4, True),
    ],
)
def test_should_double(id_num, current_index, result):
    assert should_double(id_num, current_index) == result


def test_get_doubled_values_result_lower_than_10():
    """
    If entry*2 is less than 10, then return entry*2
    """
    assert get_doubled_values("1") == 2


def test_get_doubled_values_result_greater_than_10():
    """
    If entry*2 is greater than 10, then return the sum of the digits of the
    doubled number
    """
    assert get_doubled_values("7") == 5


@pytest.mark.parametrize(
    "id_num, result",
    [
        ("1762483", True),
        ("1762484", False),
        ("1234566", True),
        ("1234565", False),
    ],
)
def test_luhn_checksum_validation(id_num, result):
    assert luhn_checksum_validation(id_num) == result