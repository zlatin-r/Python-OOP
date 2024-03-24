from unittest import TestCase, main

from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Audi", "A4", 6.7, 80)

    def test_correct_init(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("A4", self.car.model)
        self.assertEqual(6.7, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_amount)
        self.assertEqual(0, self.car.fuel_amount)




if __name__ == '__main__':
    main()
