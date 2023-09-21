import unittest

from challenge import reverseWordsInString


class TestChallenge(unittest.TestCase):

    def test_one_string(self):
        self.assertEqual(reverseWordsInString("Hello"), "Hello")
    

    def test_two_strings(self):
        self.assertEqual(reverseWordsInString("Hello World"), "World Hello")
    
    def test_two_strings_with_extra_spaces(self):
        self.assertEqual(reverseWordsInString("Hello   World"), "World   Hello")
    
    def test_three_strings(self):
        self.assertEqual(reverseWordsInString("Hello World Python"), "Python World Hello")
    
    def test_three_strings_with_extra_spaces(self):
        self.assertEqual(reverseWordsInString("Hello   World   Python"), "Python   World   Hello")
    
    def test_four_strings(self):
        self.assertEqual(reverseWordsInString("Hello World Python Java"), "Java Python World Hello")
    
    def test_four_strings_with_extra_spaces(self):
        self.assertEqual(reverseWordsInString("Hello   World   Python   Java"), "Java   Python   World   Hello")
    
    def test_example_13(self):
        self.assertEqual(reverseWordsInString("this      string     has a     lot of   whitespace"), "whitespace   of lot     a has     string      this")
    
    def test_example_15(self):
        self.assertEqual(reverseWordsInString("test        "), "        test")

if __name__ == '__main__':
    unittest.main()

"""
"this      string     has a     lot of   whitespace"
"whitespace   of lot     a has     string      this"
"""