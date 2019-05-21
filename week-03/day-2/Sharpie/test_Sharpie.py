import unittest
from Sharpie import Sharpie

class test_Sharpie(unittest.TestCase):
    def setUp(self):
        self.sharpie1 = Sharpie("Black", 5, 75)

    def test_Sharpie_color(self):
        self.assertEqual(self.sharpie1.color, "Black")

    def test_Sharpie_color_T(self):
        self.assertTrue(self.sharpie1.color == "Black")

    def test_Sharpie_use(self):
        self.assertEqual(self.sharpie1.use(), 70)

if __name__ == '__main__':
    unittest.main()