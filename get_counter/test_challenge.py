import unittest

from challenge import get_counter


class TestGetCounter(unittest.TestCase):

    def test_array_with_one_element(self):
        array = [1]
        expected = {1: 1}
        self.assertEqual(get_counter(array), expected)

    def test_array_with_two_elements(self):
        array = [1, 2]
        expected = {1: 1, 2: 1}
        self.assertEqual(get_counter(array), expected)
    
    def test_array_with_two_equal_elements(self):
        array = [1, 1]
        expected = {1: 2}
        self.assertEqual(get_counter(array), expected)
    
    def test_array_with_three_elements(self):
        array = [1, 2, 3]
        expected = {1: 1, 2: 1, 3: 1}
        self.assertEqual(get_counter(array), expected)
    
    def test_array_with_three_equal_elements(self):
        array = [1, 1, 1]
        expected = {1: 3}
        self.assertEqual(get_counter(array), expected)


if __name__=='__main__':
    unittest.main()
