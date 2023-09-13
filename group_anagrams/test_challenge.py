import unittest

from challenge import groupAnagrams


class Test(unittest.TestCase):

    def test_one_word_list(self):
        self.assertEqual(groupAnagrams(["zxc"]), [["zxc"]])


    def test_two_words_anagrams(self):
        self.assertEqual(groupAnagrams(["zxc", "cxz"]), [["zxc", "cxz"]])
    
    def test_two_words_not_anagrams(self):
        self.assertEqual(groupAnagrams(["zxc", "asd"]), [["zxc"], ["asd"]])
    
    def test_three_words_two_anagrams(self):
        self.assertEqual(groupAnagrams(["zxc", "asd", "cxz"]), [["zxc", "cxz"], ["asd"]])
    
    def test_three_words_three_anagrams(self):
        self.assertEqual(groupAnagrams(["zxc", "xzc", "cxz"]), [["zxc", "xzc", "cxz"]])

if __name__ == '__main__':
    unittest.main()