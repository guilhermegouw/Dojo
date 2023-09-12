import unittest

from challenge import semordnilap


class Test(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(semordnilap([]), [])

    def test_one_element_list(self):
        self.assertEqual(semordnilap(['element']), [])

    def test_two_elements_one_semordnilap_pair(self):
        self.assertEqual(semordnilap(['abc', 'cba']), [['abc', 'cba']])
    
    def test_two_elements_no_semordnilap_pair(self):
        self.assertEqual(semordnilap(["aaa", "bbbb"]), [])


if __name__ == "__main__":
    unittest.main()
