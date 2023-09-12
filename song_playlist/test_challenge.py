import unittest

from challenge import show_playlist


class TestShowPlaylist(unittest.TestCase):

    def test_button_four_pressed_once(self):
        self.assertEqual(show_playlist('41'), 'A, B, C, D, E')

    def test_button_one_pressed_once(self):
        self.assertEqual(show_playlist('11', '41'), 'B, C, D, E, A')

    def test_button_one_pressed_twice(self):
        self.assertEqual(show_playlist('12', '41'), 'C, D, E, A, B')

    def test_button_two_pressed_once(self):
        self.assertEqual(show_playlist('21', '41'), 'E, A, B, C, D')

    def test_button_two_pressed_twice(self):
        self.assertEqual(show_playlist('22', '41'), 'D, E, A, B, C')

    def test_button_three_pressed_once(self):
        self.assertEqual(show_playlist('31', '41'), 'B, A, C, D, E')

    def test_button_three_pressed_twice(self):
        self.assertEqual(show_playlist('32', '41'), 'A, B, C, D, E')
    
    def test_button_one_pressed_once_and_btn_two_pressed_once(self):
        self.assertEqual(show_playlist('11', '21', '41'), 'A, B, C, D, E')


if __name__=='__main__':
    unittest.main()
