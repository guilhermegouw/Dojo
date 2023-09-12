import unittest

from challenge import sentence_decoder


class TestSentenceDecoder(unittest.TestCase):

    def test_only_one_consonant(self):
        self.assertEqual(sentence_decoder('b'), 'b')
    
    def test_only_one_vowel(self):
        self.assertEqual(sentence_decoder('apa'), 'a')
    
    def test_only_one_vowel_one_consonant(self):
        self.assertEqual(sentence_decoder('apab'), 'ab')

    def test_whole_sentence(self):
        self.assertEqual(sentence_decoder('ipi lipikepe yopoupu'), 'i like you')


if __name__=="__main__":
    unittest.main()
