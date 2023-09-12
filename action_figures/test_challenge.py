import unittest

from challenge import can_organize


class TestCanOrganize(unittest.TestCase):

    def test_two_boxes_can_organize_yes(self):
        self.assertEqual(can_organize(2, (2, 1, 2), (2, 3, 4)), 'YES')

    def test_two_boxes_can_organize_no(self):
        self.assertEqual(can_organize(2, (2, 1, 3), (2, 2, 4)), 'NO')

    def test_three_boxes_can_organize_yes(self):
        self.assertEqual(can_organize(3, (2, 1, 2), (2, 3, 4), (1, 5)), 'YES')

    def test_three_boxes_can_organize_no(self):
        self.assertEqual(can_organize(3, (2, 1, 2), (2, 3, 6), (1, 5)), 'NO')


if __name__=='__main__':
    unittest.main()
