import unittest

from challenge import get_greatest_number


class TestGetGreatestNumber(unittest.TestCase):

    def test_single_element_array(self):
        self.assertEqual(get_greatest_number([1]), 1)

    def test_two_elements_array(self):
        self.assertEqual(get_greatest_number([1, 2]), 2)

    def test_three_elements_array(self):
        self.assertEqual(get_greatest_number([1, 2, 3]), 3)

    def test_four_elements_array(self):
        self.assertEqual(get_greatest_number([4, 1, 2, 3]), 4)


if __name__=='__main__':
    unittest.main()
