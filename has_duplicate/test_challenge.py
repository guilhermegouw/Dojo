import unittest

from challenge import has_duplicate_quadratic, has_duplicated_with_list, has_duplicate_dict


class TestHasDuplicateQuadratic(unittest.TestCase):
    
    def test_one_element(self):
        self.assertEqual(has_duplicate_quadratic([1]), False)

    def test_two_elements_no_duplicate(self):
        self.assertEqual(has_duplicate_quadratic([1, 2]), False)

    def test_two_elements_duplicated(self):
        self.assertEqual(has_duplicate_quadratic([1, 1]), True)

    def test_three_elements_one_duplicate(self):
        self.assertEqual(has_duplicate_quadratic([1, 2, 1]), True)

    def test_four_elements_one_duplicate(self):
        self.assertEqual(has_duplicate_quadratic([1, 2, 3, 1]), True)


class TestHasDuplicateList(unittest.TestCase):
    
    def test_one_element(self):
        self.assertEqual(has_duplicated_with_list([1]), False)

    def test_two_elements_no_duplicate(self):
        self.assertEqual(has_duplicated_with_list([1, 2]), False)

    def test_two_elements_duplicated(self):
        self.assertEqual(has_duplicated_with_list([1, 1]), True)

    def test_three_elements_one_duplicate(self):
        self.assertEqual(has_duplicated_with_list([1, 2, 1]), True)

    def test_four_elements_one_duplicate(self):
        self.assertEqual(has_duplicated_with_list([1, 2, 3, 1]), True)


class TestHasDuplicateDict(unittest.TestCase):
    
    def test_one_element(self):
        self.assertEqual(has_duplicate_dict([1]), False)

    def test_two_elements_no_duplicate(self):
        self.assertEqual(has_duplicate_dict([1, 2]), False)

    def test_two_elements_duplicated(self):
        self.assertEqual(has_duplicate_dict([1, 1]), True)

    def test_three_elements_one_duplicate(self):
        self.assertEqual(has_duplicate_dict([1, 2, 1]), True)

    def test_four_elements_one_duplicate(self):
        self.assertEqual(has_duplicate_dict([1, 2, 3, 1]), True)


if __name__=='__main__':
    unittest.main()
