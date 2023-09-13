import unittest

from challenge import validIPAddresses


class TestProgram(unittest.TestCase):

    def test_case_length_4(self):
        string = "1923"
        expected = [
            "1.9.2.3",
        ]
        self.assertEqual(validIPAddresses(string), expected)


if __name__ == "__main__":
    unittest.main()
