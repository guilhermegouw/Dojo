import unittest

from challenge import caesarCipherEncryptor


class TestCaesarCipherEncryptor(unittest.TestCase):
    def test_example(self):
        self.assertEqual(caesarCipherEncryptor('xyz', 2), 'zab')
    
    def test_key_1(self):
        self.assertEqual(caesarCipherEncryptor('abc', 1), 'bcd')
    
    def test_key_26(self):
        self.assertEqual(caesarCipherEncryptor('abc', 26), 'abc')


if __name__ == '__main__':
    unittest.main()
