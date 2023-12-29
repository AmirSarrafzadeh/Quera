import unittest
import sys
sys.path.append('../Initial_project')
from railway import Trip, Passenger, Train


class TestTrip(unittest.TestCase):

    def test_call(self):
        train = Train(last_visited_city='Sanandaj', weight_capacity=888, is_on_trip=False)
        passenger1 = Passenger(fullname='Ali Saeedi', load_weight=616)
        passenger2 = Passenger(fullname='Abolfazl Zandi', load_weight=349)
        trip = Trip(origin_city='Sanandaj', destination_city='Rasht', train=train)

        self.assertEqual(trip(), 888)

        passenger1.attend_trip(trip)
        self.assertEqual(trip(), 888 - 616)

        passenger1.attend_trip(trip)
        passenger2.attend_trip(trip)

        print(11)
        self.assertEqual(trip(), 888 - 616 - 349)
        print(12)


class TestPassenger(unittest.TestCase):

    def test_str(self):
        passenger1 = Passenger(fullname='Ali Saeedi', load_weight=616)
        self.assertEqual(str(passenger1), 'Ali Saeedi')


if __name__ == '__main__':
    unittest.main()
