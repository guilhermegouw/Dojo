import unittest

from challenge import commonCharacters


class TestChallenge(unittest.TestCase):
    
    def test_should_return_empty_list_for_no_common_chars(self):
        self.assertEqual(commonCharacters(["abc", "def"]), [])
        
    def test_should_return_one_char_for_one_string(self):
        self.assertEqual(commonCharacters(["a"]), ["a"])
    
    def test_should_return_common_chars(self):
        self.assertEqual(commonCharacters(["ab", "bc"]), ["b"])
    
    def test_should_return_common_chars_for_three_strings(self):
        self.assertEqual(commonCharacters(["abc", "bc", "cd"]), ["c"])


if __name__ == "__main__":
    unittest.main()
