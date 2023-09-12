import unittest
from number_guessing_game import check_guess


class TestCheckGuess(unittest.TestCase):
    def test_guess_not_a_number(self):
        self.assertEqual(check_guess("hello", 5), "Please enter a number between 0 and 100.")

    def test_guess_less_than_zero(self):
        self.assertEqual(check_guess(-1, 5), "Please enter a number between 0 and 100.")

    def test_guess_greater_than_100(self):
        self.assertEqual(check_guess(101, 5), "Please enter a number between 0 and 100.")
    
    def test_guess_too_high(self):
        self.assertEqual(check_guess(10, 5), "Too high!")

    def test_guess_too_low(self):
        self.assertEqual(check_guess(2, 5), "Too low!")

    def test_guess_just_right(self):
        self.assertEqual(check_guess(5, 5), "Just right!")


if __name__ == "__main__":
    unittest.main()
