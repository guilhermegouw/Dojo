import unittest

from challenge import get_bonuses_awarded


class TestGetBonusesAwarded(unittest.TestCase):

    def test_4_franchisees_1_day_1_bonus(self):
        self.assertEqual(get_bonuses_awarded(4, 1, '4 5 1 3'), 1)

    def test_4_franchisees_1_day_2_bonus(self):
        self.assertEqual(get_bonuses_awarded(4, 1, '8 10 2 6'), 2)

    def test_4_franchisees_2_day_2_bonus(self):
        self.assertEqual(get_bonuses_awarded(4, 2, '4 5 1 3', '4 5 1 3'), 2)

    def test_4_franchisees_3_days_3_bonus(self):
        self.assertEqual(get_bonuses_awarded(4, 2, '4 5 1 3', '4 5 1 3', '5 5 1 3'), 3)

    def test_example(self):
        self.assertEqual(get_bonuses_awarded(6, 4, '1 13 2 1 1 8', '2 12 10 5 11 4', '39 6 13 52 3 3', '15 8 6 2 7 14'), 9)


if __name__=="__main__":
    unittest.main()

"""
days| 0  | 1  | 2  | 3 | 4   | 5  | totals
------------------------------------------
1   | 1  | 13 | 2  | 1  | 1  | 8  | 26    | 2
2   | 2  | 12 | 10 | 5  | 11 | 4  | 44    | 0
3   | 39 | 6  | 13 | 52 | 3  | 3  | 116   | 0
4   | 15 | 8  | 6  | 2  | 7  | 14 | 52    | 4
----------------------------------------------
     0   | 3  | 0  | 0  | 0  | 0  | 

bonuses = 9
"""