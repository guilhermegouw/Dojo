import unittest

from challenge import is_more_money_needed_to_raised


class TestIsMoreMoneyNeeded(unittest.TestCase):

    def test_brunch_costs_17_dollars_1_student_for_each_year(self):
        self.assertEqual(is_more_money_needed_to_raised(17, (0.25, 0.25, 0.25, 0.25), 4), 'NO')

    def test_brunch_costs_17_dollars_4_students_first_year(self):
        self.assertEqual(is_more_money_needed_to_raised(17, (1, 0, 0, 0), 4), 'NO')

    def test_brunch_costs_17_dollars_4_students_second_year(self):
        self.assertEqual(is_more_money_needed_to_raised(17, (0, 1, 0, 0), 4), 'NO')

    def test_brunch_costs_17_dollars_4_students_third_year(self):
        self.assertEqual(is_more_money_needed_to_raised(17, (0, 0, 1, 0), 4), 'YES')

    def test_brunch_costs_17_dollars_4_students_fourth_year(self):
        self.assertEqual(is_more_money_needed_to_raised(17, (0, 0, 0, 1), 4), 'YES')

    def test_example(self):
        self.assertEqual(is_more_money_needed_to_raised(504, (0.2, 0.08, 0.4, 0.32), 125), 'YES')


if __name__=="__main__":
    unittest.main()


"""
first_year = 1 => 12
second_year = 1 => 10
third_year = 1 => 7
fourth_year = 1 => 5

total money is first_year + second_year + third_year + fourth_year = 12 + 10 + 7 + 5 => 34
50% for the brunch = 17
50% for the trip = 17

output = NO
"""