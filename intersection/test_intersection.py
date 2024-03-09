import unittest

from intersection import intersection


class TestIntersection(unittest.TestCase):
    def test_intersection_2_arrays_of_1_element(self):
        self.assertEqual(intersection([1], [1]), [1])

    def test_intersection_2_arrays_of_2_elements(self):
        self.assertEqual(intersection([1, 2], [1, 2]), [1, 2])

    def test_intersection_2_arrays_of_2_distinct_elements(self):
        self.assertEqual(intersection([1, 2], [3, 4]), [])

    def test_intersection_2_arrays_of_2_elements_with_1_element_in_common(self):
        self.assertEqual(intersection([1, 2], [2, 3]), [2])

    def test_intersection_2_arrays_of_3_elements_with_2_elements_in_common(self):
        self.assertEqual(intersection([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_intersection_arrays_different_length(self):
        self.assertEqual(intersection([1, 2, 3], [3, 4]), [3])


if __name__ == "__main__":
    unittest.main()
