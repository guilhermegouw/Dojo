import unittest

from challenge import get_common_words


class TestGetCommonWords(unittest.TestCase):

    def test_one_word_k_1(self):
        self.assertEqual(get_common_words(1, 'guilherme'), ['guilherme'])

    def test_one_word_k_2(self):
        self.assertEqual(get_common_words(2, 'guilherme'), None)

    def test_two_equal_words_plus_one_different_k_2(self):
        self.assertEqual(get_common_words(2, 'guilherme', 'guilherme', 'luciana'), ['luciana'])

    def test_two_equal_words_plus_one_different_k_1(self):
        self.assertEqual(get_common_words(1, 'guilherme', 'guilherme', 'luciana'), ['guilherme'])
if __name__=='__main__':
    unittest.main()
