import unittest

from solution_2 import is_valid_subsequence


class TestIsValidSubsequence(unittest.TestCase):
    def test_sequence_with_one_item(self):
        array = [1, 2, 3, 4]
        sequence = [1]

        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_sequence_with_two_items_valid(self):
        array = [1, 2, 3, 4]
        sequence = [1, 3]

        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_sequence_with_two_items_invalid(self):
        array = [1, 2, 3, 4]
        sequence = [1, 5]

        self.assertFalse(is_valid_subsequence(array, sequence))

    def test_sequence_with_three_items_valid(self):
        array = [1, 2, 3, 4]
        sequence = [1, 3, 4]

        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_sequence_with_three_items_invalid(self):
        array = [1, 2, 3, 4]
        sequence = [1, 3, 5]

        self.assertFalse(is_valid_subsequence(array, sequence))


if __name__ == "__main__":
    unittest.main()
