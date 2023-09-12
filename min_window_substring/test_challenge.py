import unittest

from challenge import MinWindowSubstring


class TestMinWindowSubstring(unittest.TestCase):
    def test_substring_len_equal_to_k_len(self):
        self.assertEqual(MinWindowSubstring(["aaabaaddae", "aed"]), "dae")

    def test_substring_len_equal_to_k_len_plus_one(self):
        self.assertEqual(MinWindowSubstring(["aabdccdbcacd", "aad"]), "aabd")

    def test_substring_len_equal_to_k_len_plus_two(self):
        self.assertEqual(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]), "aksfaje")


if __name__ == "__main__":
    unittest.main()
