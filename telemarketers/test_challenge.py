from challenge import is_telemarketer

import unittest


class TestIsTelemarketer(unittest.TestCase):
    def test_first_digit_not_8_or_9(self):
        self.assertEqual(is_telemarketer('1', '2', '3', '4'), 'answer')
    
    def test_first_digit_8_but_second_and_third_not_equal(self):
        self.assertEqual(is_telemarketer('8', '2', '3', '4'), 'answer')

    def test_first_digit_9_but_second_and_third_not_equal(self):
        self.assertEqual(is_telemarketer('9', '2', '3', '4'), 'answer')

    def test_first_digit_8_and_second_third_are_equal_but_fourth_not_8_or_9(self):
        self.assertEqual(is_telemarketer('8', '2', '2', '4'), 'answer')

    def test_first_digit_9_and_second_third_are_equal_but_fourth_not_8_or_9(self):
        self.assertEqual(is_telemarketer('9', '2', '2', '4'), 'answer')

    def test_first_digit_8_and_second_third_are_equal_and_fourth_is_8(self):
        self.assertEqual(is_telemarketer('8', '2', '2', '8'), 'ignore')

    def test_first_digit_9_and_second_third_are_equal_and_fourth_is_9(self):
        self.assertEqual(is_telemarketer('9', '2', '2', '9'), 'ignore')

    def test_first_digit_8_and_second_third_are_equal_and_fourth_is_9(self):
        self.assertEqual(is_telemarketer('8', '2', '2', '9'), 'ignore')

    def test_first_digit_9_and_second_third_are_equal_and_fourth_is_8(self):
        self.assertEqual(is_telemarketer('9', '2', '2', '8'), 'ignore')


if __name__=="__main__":
    unittest.main()
