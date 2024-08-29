from challenge import word_counter


def test_one_word():
    assert word_counter("hello") == 1


def test_two_words():
    assert word_counter("hello world") == 2


def test_three_words():
    assert word_counter("hello beautiful world") == 3
