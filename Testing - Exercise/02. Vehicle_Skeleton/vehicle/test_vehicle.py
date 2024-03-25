from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(self.vehicle.fuel_consumption == self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_if_fuel_is_less_than_needed_expected_raise_exception(self):
        self.vehicle.fuel = 1
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_if_fuel_is_enough_expected_fuel_decrease(self):
        self.vehicle.drive(10)

        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_not_to_fill_full_tank(self):
        self.vehicle.fuel = 50
        self.vehicle.capacity = 100

        self.vehicle.refuel(10)

        self.assertEqual(60, self.vehicle.fuel)

    def test_str_method_message(self):
        expected_message = "The vehicle has 200 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_message, self.vehicle.__str__())


if __name__ == '__main__':
    main()
