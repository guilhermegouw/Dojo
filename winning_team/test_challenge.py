from challenge import winning_team

import unittest

class TestWinningTeam(unittest.TestCase):
    def test_apple_winner(self):
        self.assertEqual(winning_team(1, 1, 1, 0, 1, 1), "A")

    def test_banana_winner(self):
        self.assertEqual(winning_team(0, 1, 1, 1, 1, 1), "B")

    def test_tie(self):
        self.assertEqual(winning_team(1, 1, 1, 1, 1, 1), "T")


if __name__ == "__main__":
    unittest.main()
