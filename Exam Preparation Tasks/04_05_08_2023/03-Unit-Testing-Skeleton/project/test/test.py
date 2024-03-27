from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Audi", "Combi", 50_000, 30_000)

    def test_correct_init(self):
        self.assertEqual("Audi", self.car.model)
        self.assertEqual("Combi", self.car.car_type)
        self.assertEqual(50_000, self.car.mileage)
        self.assertEqual(30_000, self.car.price)

    def test_setter_price_value_equal_to_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_setter_price_zero_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_setter_mileage_value_less_than_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_setter_mileage_hundred_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promotional_price_new_price_bigger_than_old_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(40_000)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_happy_case_price_set_to_new_price_returns_string(self):
        res = self.car.set_promotional_price(29_000)

        self.assertEqual(self.car.price, 29_000)
        self.assertEqual(res, "The promotional price has been successfully set.")

    def test_need_repair_price_bigger_than_car_price_divided_to_two_returns_string(self):
        res = self.car.need_repair(15_001, "Engine Change")

        self.assertEqual("Repair is impossible!", res)

    def test_need_repair_increase_car_price_add_description_to_repairs_returns_string(self):
        res = self.car.need_repair(15_000, "New Paint Job")

        self.assertEqual("Price has been increased due to repair charges.", res)
        self.assertEqual(self.car.price, 45_000)

    def test__gt__type_missmatch(self):
        car1 = SecondHandCar("BMW", "Sedan", 100_000, 100_000)
        car2 = SecondHandCar("BMW", "Combi", 100_000, 100_000)

        self.assertEqual(car1 > car2, "Cars cannot be compared. Type mismatch!")

    def test__gt__happy_case(self):
        car1 = SecondHandCar("BMW", "Combi", 100_000, 2)
        car2 = SecondHandCar("BMW2", "Combi", 100_000, 3)

        self.assertFalse(car1 > car2)
        self.assertTrue(car2 > car1)

    def test__str__no_repairs(self):



if __name__ == '__main__':
    main()
