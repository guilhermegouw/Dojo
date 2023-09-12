import unittest

from challenge import firstNonRepeatingCharacter


class Test(unittest.TestCase):

    def test_1_char_string(self):
        self.assertEqual(firstNonRepeatingCharacter("a"), 0)

    def test_2_equal_chars_string(self):
        self.assertEqual(firstNonRepeatingCharacter("aa"), -1)
    
    def test_3_chars_string(self):
        self.assertEqual(firstNonRepeatingCharacter("aba"), 1)

if __name__ == "__main__":
    unittest.main()
