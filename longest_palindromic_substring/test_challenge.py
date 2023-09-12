import unittest

from challenge import longestPalindromicSubstring


class Test(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(longestPalindromicSubstring('a'), 'a')

    def test_two_equeal_characters(self):
        self.assertEqual(longestPalindromicSubstring('aa'), 'aa')

    def test_two_equeal_characters_one_different(self):
        self.assertEqual(longestPalindromicSubstring('baa'), 'aa')
    
    def test_example_1(self):
        self.assertEqual(longestPalindromicSubstring('abaxyzzyxf'), 'xyzzyx')


if __name__ == '__main__':
    unittest.main()