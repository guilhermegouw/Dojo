import unittest

from challenge import get_both_days_occupied_parking_spaces


class TestOccupiedSpaces(unittest.TestCase):

    def test_1_space_not_occupied_both_days(self):
        self.assertEqual(get_both_days_occupied_parking_spaces(1, '.', '.'), 0)

    def test_1_space_occupied_both_days(self):
        self.assertEqual(get_both_days_occupied_parking_spaces(1, 'C', 'C'), 1)

    def test_2_spaces_one_occupied_both_days(self):
        self.assertEqual(get_both_days_occupied_parking_spaces(2, 'C.', 'C.'), 1)

    def test_2_spaces_none_occupied_both_days(self):
        self.assertEqual(get_both_days_occupied_parking_spaces(2, '.C', 'C.'), 0)

    def test_3_spaces_2_occupied_both_days_version_1(self):
        self.assertEqual(get_both_days_occupied_parking_spaces(3, 'CC.', 'CC.'), 2)

    def test_3_spaces_2_occupied_both_days_version_2(self):
        self.assertEqual(get_both_days_occupied_parking_spaces(3, 'C.C', 'C.C'), 2)


if __name__=="__main__":
    unittest.main()
