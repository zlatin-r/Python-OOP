from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Jo", 1.40)

    def test_init(self):
        self.assertEqual("Jo", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0.0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_setter_earned_money_value_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Jo went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_location_in_available_cargos_raises_exception(self):
        self.driver.available_cargos = {"Cargo 1": 10}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Cargo 1", 10)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_happy_case(self):
        res = self.driver.add_cargo_offer("Cargo 2", 5)
        expect = f"Cargo for 5 to Cargo 2 was added as an offer."

        self.assertEqual({"Cargo 2": 5}, self.driver.available_cargos)
        self.assertEqual(expect, res)

    def test_drive_best_cargo_offer_no_offers_available_raises_value_error(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("California", 2000)
        self.driver.add_cargo_offer("Los Angeles", 20000)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.driver.name} is driving 20000 to Los Angeles.")
        self.assertEqual(self.driver.earned_money, 4000)
        self.assertEqual(self.driver.miles, 20000)

    def test_eat_every_250_miles_earned_money_decrease_with_20(self):
        self.driver.earned_money = 100

        self.driver.eat(250)

        self.assertEqual(80, self.driver.earned_money)

    def test_sleep_every_1000_miles_earned_money_decrease_with_45(self):
        self.driver.earned_money = 100

        self.driver.sleep(1000)

        self.assertEqual(55, self.driver.earned_money)

    def test_pump_gas_every_1500_miles_earned_money_decrease_with_500(self):
        self.driver.earned_money = 1000

        self.driver.pump_gas(1500)

        self.assertEqual(500, self.driver.earned_money)

    def test_repair_truck_every_10_000_miles_earned_money_decrease_with_7500(self):
        self.driver.earned_money = 10_000

        self.driver.repair_truck(10_000)

        self.assertEqual(2_500, self.driver.earned_money)

    def test__repr__(self):
        self.assertEqual("Jo has 0 miles behind his back.", self.driver.__repr__())


if __name__ == '__main__':
    main()
