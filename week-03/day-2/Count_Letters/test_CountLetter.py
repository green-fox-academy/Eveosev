import unittest
from Count_Letters import count_letters

class test_count_letters(unittest.TestCase):
    def test_count_letters(self):
        self.assertEqual(count_letters("dog"), {"d":1, "o":1, "g":1})

if __name__ == "__main__":
    unittest.main()