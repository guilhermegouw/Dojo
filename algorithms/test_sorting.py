import unittest

from sorting import (
    bubble_sort,
    my_sort,
    selection_sort,
    insertion_sort,
    insertion_sort_book,
)


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


class TestSelectionSort(unittest.TestCase):
    def test_one_element_list(self):
        self.assertEqual(selection_sort([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(selection_sort([2, 1]), [1, 2])

    def test_three_elements_list(self):
        self.assertEqual(selection_sort([3, 2, 1]), [1, 2, 3])

    def test_four_elements_list(self):
        self.assertEqual(selection_sort([0, 3, 2, 1]), [0, 1, 2, 3])

    def test_five_elements_list(self):
        self.assertEqual(selection_sort([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])


class TestInsertionSort(unittest.TestCase):
    def test_one_element_list(self):
        self.assertEqual(insertion_sort([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(insertion_sort([2, 1]), [1, 2])

    def test_three_elements_list(self):
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])

    def test_four_elements_list(self):
        self.assertEqual(insertion_sort([0, 3, 2, 1]), [0, 1, 2, 3])

    def test_five_elements_list(self):
        self.assertEqual(insertion_sort([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])


class TestInsertionBookSort(unittest.TestCase):
    def test_one_element_list(self):
        self.assertEqual(insertion_sort_book([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(insertion_sort_book([2, 1]), [1, 2])

    def test_three_elements_list(self):
        self.assertEqual(insertion_sort_book([3, 2, 1]), [1, 2, 3])

    def test_four_elements_list(self):
        self.assertEqual(insertion_sort_book([0, 3, 2, 1]), [0, 1, 2, 3])

    def test_five_elements_list(self):
        self.assertEqual(insertion_sort_book([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])


if __name__ == "__main__":
    unittest.main()
