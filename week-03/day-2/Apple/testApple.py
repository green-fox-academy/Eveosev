import unittest
from Apple import Apple

class test_Apple(unittest.TestCase):
    def setUp(self):
        self.myobject = Apple()

    def test_get_apple(self):
        self.assertEquals(self.myobject.get_apple(), 'apple')
    
    def test_get_apple_failing(self):
        self.assertEquals(self.myobject.get_apple(), 'APPLE')

    def test_get_apple_correct_failingcast(self):
        self.assertEquals(self.myobject.get_apple(), 'APPLE'.lower())

if __name__ == '__main__':
    unittest.main()