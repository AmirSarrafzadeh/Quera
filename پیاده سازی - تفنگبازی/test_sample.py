import unittest
from Shooter import Shooter


class TestFind(unittest.TestCase):

    def test1(self):
        shooter1 = Shooter()

        shooter1.set_gun_by_name("Submachine Gun")
        shooter1.add_bullet_of_given_size_to_gun(0.5, 1)
        self.assertEqual(shooter1.shoot_to_target(1, 1, 20, 5, 4), 10)

if __name__ == '__main__':
    unittest.main()
