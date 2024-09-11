import pytest
from challenge import decode_luka


@pytest.mark.parametrize(
    "sentence, expected",
    [("ipi", "i"), ("p", "p"), ("ipi lipi", "i li")],
)
def test_decode_luka(sentence, expected):
    assert decode_luka(sentence) == expected
