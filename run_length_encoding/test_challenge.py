import unittest

from challenge import runLengthEncoding


class TestRunLengthEncoding(unittest.TestCase):
    def test_one_character(self):
        self.assertEqual(runLengthEncoding('a'), '1a')
    
    def test_two_characters(self):
        self.assertEqual(runLengthEncoding('aa'), '2a')
    
    def test_three_characters(self):
        self.assertEqual(runLengthEncoding('aab'), '2a1b')
    
    def test_multiple_characters_reoccuring_char(self):
        self.assertEqual(runLengthEncoding("************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"), '9*3*7^6$7%6!9A9A2A')


if __name__ == '__main__':
    unittest.main()
