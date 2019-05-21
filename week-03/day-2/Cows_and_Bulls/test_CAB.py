import unittest
from CAB import cab

class test_CAB(unittest.TestCase):
    def setUp(self):
        self.cab1 = cab()
    
    def test_game_state(self):
        self.assertEqual(self.cab1.state, "playing")

    def test_guess(self):
        self.assertEqual(self.cab1.guess(6752), "3 cow 1 bull")

if __name__ == "__main__":
    unittest.main()