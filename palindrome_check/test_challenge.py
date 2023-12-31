import unittest

from challenge import isPalindrome


class TestPalindrome(unittest.TestCase):
    def test_single_character(self):
        self.assertTrue(isPalindrome('a'), True)

    def test_two_characters(self):
        self.assertTrue(isPalindrome('aa'), True)
    
    def test_two_characters_False(self):
        self.assertFalse(isPalindrome('ab'), False)

    def test_three_characters(self):
        self.assertTrue(isPalindrome('aba'), True)

    def test_three_characters_False(self):
        self.assertFalse(isPalindrome('abc'), False)

    def test_example(self):
        self.assertEqual(isPalindrome('abcdcba'), True)

if __name__ == '__main__':
    unittest.main()