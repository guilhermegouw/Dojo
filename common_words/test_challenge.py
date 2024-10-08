import pytest
from challenge import get_kth_most_common_words


@pytest.mark.parametrize(
    ("words", "k", "expected"),
    [
        (["first"], 1, ["first"]),
        (
            ["apple", "banana", "apple", "orange", "banana", "banana"],
            1,
            ["banana"],
        ),
        (
            ["apple", "banana", "apple", "orange", "banana", "banana"],
            2,
            ["apple"],
        ),
        (
            ["apple", "banana", "orange"],
            1,
            ["apple", "banana", "orange"],
        ),
        (["apple", "banana", "orange"], 2, []),
        (["a", "a", "b", "b", "c"], 2, ["c"]),
        (["a", "b", "c", "d"], 5, []),
    ],
)
def test_get_kth_most_common_words(words, k, expected):
    assert get_kth_most_common_words(words, k) == expected
