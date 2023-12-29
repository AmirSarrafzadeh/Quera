import unittest
import sys
sys.path.append('../Initial_project')
from peydayesh import find


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual(4, find(1, 2, 3))

	def test_2(self):
		self.assertEqual(2, find(1, 4, 3))
  
if __name__ == '__main__':
    unittest.main()