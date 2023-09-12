import unittest

from challenge import get_scores


class TestGetScores(unittest.TestCase):

    def test_2_cards_deck_no_points(self):
        self.assertEqual(get_scores(['two', 'three']), (0, 0))

    def test_2_cards_deck_one_point_for_a(self):
        self.assertEqual(get_scores(['jack', 'three']), (1, 0))

    def test_3_cards_deck_one_point_for_a(self):
        self.assertEqual(get_scores(['jack', 'three', 'four']), (1, 0))

    def test_3_cards_deck_one_point_for_b(self):
        self.assertEqual(get_scores(['three', 'jack', 'four']), (0, 1))

    def test_3_cards_deck_two_points_for_a(self):
        self.assertEqual(get_scores(['queen', 'three', 'four']), (2, 0))

    def test_4_cards_deck_two_points_for_b(self):
        self.assertEqual(get_scores(['three', 'queen', 'four', 'five']), (0, 2))

    def test_4_cards_deck_three_points_for_a(self):
        self.assertEqual(get_scores(['king', 'two', 'four', 'five']), (3, 0))

    def test_5_cards_deck_three_points_for_b(self):
        self.assertEqual(get_scores(['six', 'king', 'two', 'four', 'five']), (0, 3))

    def test_5_cards_deck_four_points_for_a(self):
        self.assertEqual(get_scores(['ace', 'six', 'two', 'four', 'five']), (4, 0))

    def test_6_cards_deck_four_points_for_a(self):
        self.assertEqual(get_scores(['seven', 'ace', 'six', 'two', 'four', 'five']), (0, 4))

    def test_example(self):
        self.assertEqual(get_scores(['queen', 'three', 'seven', 'king', 'nine', 'jack', 'eight', 'king', 'jack', 'four']), (3, 1))


if __name__=="__main__":
    unittest.main()
