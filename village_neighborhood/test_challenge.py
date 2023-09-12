import unittest

from challenge import get_size_of_smallest_neighborhood


class TestGetSmallestNeighborhoodSize(unittest.TestCase):

    def test_2_villages(self):
        self.assertEqual(get_size_of_smallest_neighborhood(2, 6, 10), 'It should contain at least 3 positions')

    def test_3_villages(self):
        self.assertEqual(get_size_of_smallest_neighborhood(3, 6, 10, 15), 4.5)

    def test_4_villages(self):
        self.assertEqual(get_size_of_smallest_neighborhood(4, 6, 10, 15, 17), 3.5)

    def test_5_villages(self):
        self.assertEqual(get_size_of_smallest_neighborhood(5, 6, 10, 15, 17, 20), 2.5)

    def test_6_villages_third_is_the_smallest(self):
        self.assertEqual(get_size_of_smallest_neighborhood(6, 6, 10, 15, 17, 20, 30), 2.5)


if __name__=='__main__':
    unittest.main()

"""
6 villages
6 10 15 17 20 30

first_neighborhood = [6 10 15] 
starts = (10 + 6)/2 => 8
ends = (10 + 15)/2 => 12.5
size = ends - starts => 12.5 - 8 = 4.5

second_neighborhood = [10 15 17] 
starts = (15 + 10)/2 => 12.5
ends = (17 + 15)/2 => 16
size = ends - starts => 16 - 12.5 = 3.5

third_neighborhood = [15 17 20] 
starts = (15 + 17)/2 => 16
ends = (17 + 20)/2 => 18.5
size = ends - starts => 18.5 - 16 = 2.5

fourth_neighborhood = [17 20 30] 
starts = (17 + 20)/2 => 18.5
ends = (20 + 30)/2 => 25
size = ends - starts => 25 - 18.5 = 6.5
"""
