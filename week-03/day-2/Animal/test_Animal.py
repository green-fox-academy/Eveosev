import unittest
from  Animal import Animal

class test_Animal(unittest.TestCase):
    def setUp(self):
        self.animal1 = Animal()

    def test_animal_hunger(self):
        self.assertEqual(self.animal1.hunger, 50)

    def test_animal_eat(self):
        self.assertEqual(self.animal1.eat(), 49)

    def test_animal_drink(self):
        self.assertEqual(self.animal1.drink(), 49)

    def test_animal_play(self):
        self.assertEqual(self.animal1.play(), "49 49")

    def test_animal_play2(self):
        self.assertEqual(self.animal1.play(), "51 51")

if __name__ == "__main__":
    unittest.main()