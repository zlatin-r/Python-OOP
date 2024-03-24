from unittest import TestCase, main

from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Audi", "A4", 6.7, 80)

    def test_correct_init(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("A4", self.car.model)
        self.assertEqual(6.7, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -12

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))


if __name__ == '__main__':
    main()
