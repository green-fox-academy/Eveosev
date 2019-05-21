import unittest
from Fibonacci import fibonacci

class test_fibonacci(unittest.TestCase):
    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), [0, 1, 1])

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), [0, 1])

    def test_fibonacci_error(self):
        self.assertEqual(fibonacci(0), "Error")

if __name__ == "__main__":
    unittest.main()
