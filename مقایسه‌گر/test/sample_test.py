import unittest
import sys
sys.path.append('../Initial_project')
from moghayeseGar import compare


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual('las', compare('ali', 'salib'))

	def test_2(self):
		self.assertEqual('Both strings are empty!', compare('nima', 'amin'))


if __name__ == '__main__':
    unittest.main()