import unittest

from challenge import get_data_available_for_next_month


class TestDataAvailableForNextMonth(unittest.TestCase):

    def test_one_month_whole_usage(self):
        self.assertEqual(get_data_available_for_next_month(10, 1, 10), 10)
    
    def test_one_month_half_usage(self):
        self.assertEqual(get_data_available_for_next_month(10, 1, 5), 15)
    
    def test_two_months(self):
        self.assertEqual(get_data_available_for_next_month(10, 2, 5, 5), 20)

    def test_three_months(self):
        self.assertEqual(get_data_available_for_next_month(10, 3, 5, 5, 5), 25)


if __name__=="__main__":
    unittest.main()