import unittest

from challenge import isValidSubsequence


class TestValidateSubsequence(unittest.TestCase):

    def test_subsequence_len_equal_1_valid(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4], [1]), True)

    def test_subsequence_len_equal_1_not_valid(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4], [5]), False)

    def test_subsequence_len_equal_2_valid(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4], [1, 3]), True)

    def test_subsequence_len_equal_2_not_valid(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4], [3, 2]), False)
    
    def test_subsequence_len_equal_3_valid(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4], [1, 2, 4]), True)
    
    def test_subsequence_len_equal_3_not_valid(self):
        self.assertEqual(isValidSubsequence([1, 2, 3, 4], [1, 2, 5]), False)
    
    def test_subsequence_len_equal_4_valid(self):
        self.assertEqual(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]), True)


if __name__ == "__main__":
    unittest.main()
