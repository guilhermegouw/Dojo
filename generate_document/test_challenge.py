import unittest

from challenge import generateDocument


class Test(unittest.TestCase):

    def test_characteres_and_documents_are_equal(self):
        self.assertTrue(generateDocument("abc", "abc"), True)

    def test_same_characteres_different_order(self):
        self.assertTrue(generateDocument("abc", "bca"), True)
    
    def test_different_characteres(self):
        self.assertFalse(generateDocument("abc", "def"), False)
    
    def test_characteres_with_spaces(self):
        self.assertTrue(generateDocument("a b c", "abc"), True)
    
    def test_characteres_with_spaces_and_different_order(self):
        self.assertTrue(generateDocument("a b c", "bca"), True)
    
    def test_example_1(self):
        self.assertFalse(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"), True)


if __name__ == "__main__":
    unittest.main()
