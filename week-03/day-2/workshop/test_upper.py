import unittest
from upper import StringMethod

class TestStringMethod(unittest.TestCase):
    def setUp(self):
        foo = StringMethod('foo')

    def test_upper(self):
        self.assertEqual(foo.upper(), 'FOO')
    
    def test_isupper(self):
        
if __name__ == '__main__':
    unittest.main()