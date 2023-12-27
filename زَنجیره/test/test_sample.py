import unittest
import sys
sys.path.append('../Initial_project')
from chain import Chain

class TestFind(unittest.TestCase):

    def test1(self):
        self.assertEqual(Chain('Ali')('Safinal')('is')('the')('best.'), 'Ali Safinal is the best.')

    def test2(self):
        self.assertEqual(Chain(2)(3)(4)(2.9)(1), 12.9)

    def test3(self):
        self.assertEqual(Chain('abc')('defg') == 'abc defg', True)

    def test4(self):
        self.assertEqual(Chain(64) == 64, True)

    def test5(self):
        self.assertEqual(Chain(64) == '64', False)

    def test6(self):
        self.assertEqual(Chain(64) == 63, False)

    def test7(self):
        self.assertEqual(Chain(64)(2)(3)(4) == 73, True)


    def test8(self):
        self.assertEqual(Chain(64)('ka;'))

    def test9(self):
        self.assertEqual(Chain('64') == '64', True)

    def test10(self):
        self.assertEqual(Chain(9)([1, 2]))

    def test11(self):
        self.assertEqual(Chain(0)(0), [0, 0])

if __name__ == '__main__':
    unittest.main()

