from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def test_init_correct(self):
        self.car = SecondHandCar('test model', 'test type', 101, 1.001)
        self.assertEqual(self.car.model, 'test model')
        self.assertEqual(self.car.car_type, 'test type')
        self.assertEqual(self.car.mileage, 101)
        self.assertEqual(self.car.price, 1.001)

    def test_wrong_price__should_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = SecondHandCar('model', 'type', 101, 1)
        self.assertEqual(str(ve.exception), "Price should be greater than 1.0!")

    def test_wrong_price_zero__should_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = SecondHandCar('model', 'type', 101, 0)
        self.assertEqual(str(ve.exception), "Price should be greater than 1.0!")

    def test_wrong_mileage_100__should_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = SecondHandCar('model', 'type', 100, 1.001)
        self.assertEqual(str(ve.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_wrong_mileage_99__should_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = SecondHandCar('model', 'type', 99, 1.001)
        self.assertEqual(str(ve.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_promotional_price_happy_case(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)

        res = self.car.set_promotional_price(1.001)
        self.assertEqual(res, "The promotional price has been successfully set.")
        self.assertEqual(self.car.price, 1.001)

    def test_promotional_price_equal_prices_should_raise(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2)
        self.assertEqual(str(ve.exception), "You are supposed to decrease the price!")

    def test_promotional_price_higher_price_should_raise(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2.001)
        self.assertEqual(str(ve.exception), "You are supposed to decrease the price!")

    def test_need_repair_happy_case__half_priced(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)

        res = self.car.need_repair(1.0, 'Oil test')
        self.assertEqual(res, "Price has been increased due to repair charges.")
        self.assertEqual(self.car.price, 3.0)
        self.assertEqual(self.car.repairs, ['Oil test'])

    def test_need_repair_happy_case__less_half_priced(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)

        res = self.car.need_repair(0.999, 'Oil test')
        self.assertEqual(res, "Price has been increased due to repair charges.")
        self.assertEqual(self.car.price, 2.999)
        self.assertEqual(self.car.repairs, ['Oil test'])

    def test_need_repair_happy_case__two_repairs_less_half_priced(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)

        res = self.car.need_repair(0.999, 'Oil test')
        self.assertEqual(res, "Price has been increased due to repair charges.")
        self.assertEqual(self.car.price, 2.999)
        self.assertEqual(self.car.repairs, ['Oil test'])

        res = self.car.need_repair(1.001, 'Air test')
        self.assertEqual(res, "Price has been increased due to repair charges.")
        self.assertEqual(self.car.price, 4)
        self.assertEqual(self.car.repairs, ['Oil test', 'Air test'])

    def test_need_repair_unhappy_case__more_than_half_priced(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)
        res = self.car.need_repair(1.001, 'Oil test')
        self.assertEqual(res, "Repair is impossible!")
        self.assertEqual(self.car.price, 2)
        self.assertEqual(self.car.repairs, [])

    def test__gt__happy_case(self):
        self.car1 = SecondHandCar('test model', 'test type', 101, 2)
        self.car2 = SecondHandCar('test model2', 'test type', 101, 3)

        self.assertFalse(self.car1 > self.car2)
        self.assertTrue(self.car2 > self.car1)

    def test__gt__type_mismatch(self):
        self.car1 = SecondHandCar('test model', 'test type1', 101, 2)
        self.car2 = SecondHandCar('test model2', 'test type2', 101, 3)

        self.assertEqual(self.car1 > self.car2, "Cars cannot be compared. Type mismatch!")

    def test__str__no_repairs(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)

        self.assertEqual(str(self.car), """Model test model | Type test type | Milage 101km
Current price: 2.00 | Number of Repairs: 0""")

    def test__str__1_repairs(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)
        self.car.need_repair(0.99, 'something')
        self.assertEqual(str(self.car), """Model test model | Type test type | Milage 101km
Current price: 2.99 | Number of Repairs: 1""")

    def test__str__2_repairs(self):
        self.car = SecondHandCar('test model', 'test type', 101, 2)
        self.car.need_repair(0.99, 'something')
        self.car.need_repair(1.41, 'something2')
        self.assertEqual(str(self.car), """Model test model | Type test type | Milage 101km
Current price: 4.40 | Number of Repairs: 2""")


if __name__ == '__main__':
    main()

