import pytest
from challenge import is_telemarketer


@pytest.mark.parametrize(
    "phone_number,expected",
    [
        ([8, 1, 1, 9], "ignore"),
        ([8, 1, 1, 1], "answer"),
        ([1, 1, 1, 9], "answer"),
        ([1, 1, 1, 1], "answer"),
    ],
)
def test_is_telemarketer(phone_number, expected):
    assert is_telemarketer(phone_number) == expected
