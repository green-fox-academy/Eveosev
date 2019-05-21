import unittest
from  Sum import Sum

class test_Sum(unittest.TestCase):

    def test_getSum(self):
        List = [1,2,3,4,5,6,7]
        testList = Sum([1,2,3,4,5,6,7])
        self.assertEqual(testList.getSum(), sum(List))

    def test_getSum_emptylist(self):
        testList = Sum([])
        self.assertEqual(testList.getSum(), sum([]))
    
    def test_getSum_oneElist(self):
        testList = Sum([43])
        self.assertEqual(testList.getSum(), sum([43]))

    def test_getSum_multiElist(self):
        testList = Sum([1,2,3,4.5,7.7])
        self.assertEqual(testList.getSum(), sum([1,2,3,4.5,7.7]))

    def test_getSum_None(self):
        testList = Sum(None)
        self.assertIsNone(testList.getSum(), None)

if __name__ == "__main__":
    unittest.main()

