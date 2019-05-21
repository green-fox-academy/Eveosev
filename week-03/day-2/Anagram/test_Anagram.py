from Anagram import Anagram
import unittest

class test_Anagram(unittest.TestCase):
    def test_Anagram_TrueStrings(self):
        self.assertTrue(Anagram("dog", "god"))

    def test_Anagram_FalseStrings(self):
        self.assertTrue(Anagram("god", "godlike"))

if __name__ == "__main__":
    unittest.main()