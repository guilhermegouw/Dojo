import unittest

from challenge import average_of_even_numbers, book_average_of_even_numbers


class TestAverageOfEvenNumbers(unittest.TestCase):
    def test_single_elem_list_no_even_number(self):
        self.assertEqual(average_of_even_numbers([1]), 0)

    def test_single_elem_list_one_even_number(self):
        self.assertEqual(average_of_even_numbers([2]), 2)

    def test_two_elements_list_one_even_number(self):
        self.assertEqual(average_of_even_numbers([1, 2]), 2)

    def test_two_elements_list_two_even_numbers(self):
        self.assertEqual(average_of_even_numbers([4, 2]), 3)

    def test_three_elements_list_three_even_numbers(self):
        self.assertEqual(average_of_even_numbers([4, 2, 6]), 4)


class TestBookAverageOfEvenNumbers(unittest.TestCase):
    def test_single_elem_list_no_even_number(self):
        self.assertEqual(book_average_of_even_numbers([1]), 0)

    def test_single_elem_list_one_even_number(self):
        self.assertEqual(book_average_of_even_numbers([2]), 2)

    def test_two_elements_list_one_even_number(self):
        self.assertEqual(book_average_of_even_numbers([1, 2]), 2)

    def test_two_elements_list_two_even_numbers(self):
        self.assertEqual(book_average_of_even_numbers([4, 2]), 3)

    def test_three_elements_list_three_even_numbers(self):
        self.assertEqual(book_average_of_even_numbers([4, 2, 6]), 4)


if __name__ == "__main__":
    unittest.main()
