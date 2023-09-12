import unittest

from challenge import get_ball_location


class TestGetBallLocation(unittest.TestCase):

    def test_one_move_type_A(self):
        self.assertEqual(get_ball_location('A'), 2)

    def test_one_move_type_B(self):
        self.assertEqual(get_ball_location('B'), 1)

    def test_one_move_type_C(self):
        self.assertEqual(get_ball_location('C'), 3)

    def test_two_equal_moves(self):
        self.assertEqual(get_ball_location('AA'), 1)

    def test_two_moves_AB(self):
        self.assertEqual(get_ball_location('AB'), 3)

    def test_three_moves_ABC(self):
        self.assertEqual(get_ball_location('ABC'), 1)


if __name__=="__main__":
    unittest.main()
