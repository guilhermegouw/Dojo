import unittest

from summing_numbers import my_sum


class TestMySum(unittest.TestCase):
    def test_my_sum_with_no_args(self):
        self.assertEqual(my_sum(), 0)
    
    def test_my_sum_with_one_arg(self):
        self.assertEqual(my_sum(5), 5)

    def test_my_sum_with_two_args(self):
        self.assertEqual(my_sum(5, 10), 15)

    def test_my_sum_with_sequences_as_args(self):
        self.assertEqual(my_sum([1, 2, 3], [4, 5]), 15)
    
    def test_my_sum_with_sequences_and_non_sequences_as_args(self):
        self.assertEqual(my_sum([1, 2, 3], 4, 5), 15)


if __name__ == "__main__":
    unittest.main()
