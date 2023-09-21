import unittest

from challenge import twoNumberSum


class TestTwoNumberSum(unittest.TestCase):

    def test_array_with_two_numbers_with_target_sum(self):
        self.assertEqual(twoNumberSum([1, 2], 3), [1, 2])

    def test_array_with_two_numbers_without_target_sum(self):
        self.assertEqual(twoNumberSum([1, 3], 3), [])

    def test_array_with_three_numbers_with_target_sum(self):
        self.assertEqual(twoNumberSum([1, 2, 3], 5), [2, 3])
    

if __name__ == '__main__':
    unittest.main()
