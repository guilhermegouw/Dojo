import unittest

from sorting import bubble_sort, my_sort


class TestBubbleSort(unittest.TestCase):

    def test_one_element_list(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(bubble_sort([2, 1]), [1, 2])

    def test_three_elements_list(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])

    def test_four_elements_list(self):
        self.assertEqual(bubble_sort([0, 3, 2, 1]), [0, 1, 2, 3])

    def test_five_elements_list(self):
        self.assertEqual(bubble_sort([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])


class TestMySort(unittest.TestCase):

    def test_one_element_list(self):
        self.assertEqual(my_sort([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(my_sort([2, 1]), [1, 2])

    def test_three_elements_list(self):
        self.assertEqual(my_sort([3, 2, 1]), [1, 2, 3])

    def test_four_elements_list(self):
        self.assertEqual(my_sort([0, 3, 2, 1]), [0, 1, 2, 3])

    def test_five_elements_list(self):
        self.assertEqual(my_sort([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])


if __name__=='__main__':
    unittest.main()
