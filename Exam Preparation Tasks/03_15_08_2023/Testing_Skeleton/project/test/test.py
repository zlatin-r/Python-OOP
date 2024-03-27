from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.traveler = Trip(100, 1, False)

    def test_init(self):
        self.assertEqual(100, self.traveler.budget)
        self.assertEqual(1, self.traveler.travelers)
        self.assertEqual(False, self.traveler.is_family)
        self.assertEqual({}, self.traveler.booked_destinations_paid_amounts)

    def test_setter_travelers_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.traveler.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_setter_is_family(self):
        self.traveler.is_family = True
        self.assertFalse(self.traveler.is_family)

    def test_book_a_trip_destination_not_found(self):
        expected = 'This destination is not in our offers, please choose a new one!'
        result = self.traveler.book_a_trip("Aytos")
        self.assertEqual(expected, result)

    # def test_book_a_trip_without_budget(self):
    #     self.t = Trip(100, 1, True)
    #
    #     res = self.t.book_a_trip("Bulgaria")
    #
    #     self.assertEqual(self.t.booked_destinations_paid_amounts, {})
    #     self.assertEqual(res, "Your budget is not enough!")

    def test_book_a_trip_destination_found_is_family_not_enough_budget(self):
        self.traveler.is_family = True
        self.traveler.budget = 1
        expected = 'Your budget is not enough!'
        result = self.traveler.book_a_trip("Brazil")
        self.assertEqual(expected, result)

    def test_book_a_trip_destination_found_is_family_enough_budget(self):
        self.t1 = Trip(10_000, 1, True)

        result = self.t1.book_a_trip("New Zealand")
        expect = f'Successfully booked destination New Zealand! Your budget left is {self.t1.budget:.2f}'

        self.assertEqual(2500, self.t1.budget)
        self.assertFalse(self.t1.is_family)
        self.assertEqual({'New Zealand': 7500}, self.t1.booked_destinations_paid_amounts)
        self.assertEqual(expect, result)

    def test_book_a_trip_happy_case_with_family_discount(self):
        self.t = Trip(25_000, 2, True)

        res = self.t.book_a_trip("Bulgaria")
        self.assertEqual(self.t.booked_destinations_paid_amounts, {"Bulgaria": 900.0})
        self.assertEqual(self.t.budget, 24100)
        self.assertEqual(res, 'Successfully booked destination Bulgaria! Your budget left is 24100.00')

    def test_booking_status_without_any_bookings(self):
        self.t1 = Trip(10_000, 1, False)

        expected = f'No bookings yet. Budget: {self.t1.budget:.2f}'
        result = self.t1.booking_status()

        self.assertEqual(expected, result)

    def test_booking_status_happy_case(self):
        self.t = Trip(1_000, 1, False)
        self.t.book_a_trip("Bulgaria")
        self.assertEqual(self.t.booked_destinations_paid_amounts, {"Bulgaria": 500})
        res = self.t.booking_status()
        self.assertEqual(res, """Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 500.00""")


if __name__ == '__main__':
    main()
