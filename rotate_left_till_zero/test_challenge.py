import unittest

from challenge import rotate_left_till_zero


class TestRotateLeftTillZero(unittest.TestCase):
    
    def test_one_element_array(self):
        self.assertEqual(rotate_left_till_zero([0]), [0])

    def test_two_element_array(self):
        self.assertEqual(rotate_left_till_zero([1, 0]), [0, 1])

    def test_three_element_array(self):
        self.assertEqual(rotate_left_till_zero([1, 2, 0]), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
