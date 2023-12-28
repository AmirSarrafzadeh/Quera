import unittest
import sys
sys.path.append('../Initial_project')
from separator import separator


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual(([-2, 0, 2], [-3, -1, 1, 3]), separator([-3, -2, -1, 0, 1, 2, 3]))

	def test_2(self):
		self.assertEqual(([], [1, 11, 5, 7, 3]), separator([1, 11, 5, 7, 3]))




if __name__ == '__main__':
    unittest.main()