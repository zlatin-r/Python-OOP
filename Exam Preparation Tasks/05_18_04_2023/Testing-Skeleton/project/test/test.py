from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.robot = Robot("1", "Education", 10, 100.00)

    def test_init(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100.00, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_setter_category_with_not_allowed_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Some Category"

        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_setter_category_happy_case(self):
        self.robot.category = "Entertainment"

        self.assertEqual("Entertainment", self.robot.category)

    def test_setter_price_with_negative_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_hardware_already_in_upgrades_returns_string(self):
        self.robot.hardware_upgrades = ["arm"]

        res = self.robot.upgrade("arm", 100)
        expect = f"Robot 1 was not upgraded."

        self.assertEqual(expect, res)

    def test_upgrade_happy_case(self):
        self.test_robot = Robot("3", "Military", 10, 1000)

        res = self.test_robot.upgrade("body", 100)
        expect = f"Robot {self.test_robot.robot_id} was upgraded with {self.test_robot.hardware_upgrades[-1]}."

        self.assertEqual(["body"], self.test_robot.hardware_upgrades)
        self.assertEqual(expect, res)

    def test_update_with_version_less_than_max_installed_raises_value_error(self):
        self.test_robot = Robot("12", "Education", 10, 100.00)
        self.test_robot.software_updates = [2.00]

        res = self.test_robot.update(1.00, 1)
        expect = "Robot 12 was not updated."

        self.assertEqual(expect, res)

    def test_update_with_version_equal_to_max_installed_raises_value_error(self):
        self.test_robot = Robot("12", "Education", 10, 100.00)
        self.test_robot.software_updates = [2.00]

        res = self.test_robot.update(2.00, 1)
        expect = "Robot 12 was not updated."

        self.assertEqual(expect, res)

    def test_update_with_correct_version_but_not_enough_capacity_raises_value_error(self):
        self.test_robot = Robot("12", "Education", 10, 100.00)
        self.test_robot.software_updates = [2.00]

        res = self.test_robot.update(2.00, 11)
        expect = "Robot 12 was not updated."

        self.assertEqual(expect, res)

    def test_update_happy_case(self):
        self.test_robot = Robot("12", "Education", 10, 100.00)
        self.test_robot.software_updates = [2.0]

        res = self.test_robot.update(3.0, 1)

        self.assertEqual([2.0, 3.0], self.test_robot.software_updates)
        self.assertEqual(9, self.test_robot.available_capacity)
        self.assertEqual("Robot 12 was updated to version 3.0.", res)

    def test__gt__first_robot_more_expensive(self):
        r1 = Robot("12", "Education", 10, 100)
        r2 = Robot("21", "Entertainment", 10, 99.99)

        res = r1 > r2

        self.assertEqual("Robot with ID 12 is more expensive than Robot with ID 21.", res)

    def test__gt__first_robot_is_cheaper(self):
        r1 = Robot("12", "Education", 10, 99.98)
        r2 = Robot("21", "Entertainment", 10, 99.99)

        res = r1 > r2

        self.assertEqual("Robot with ID 12 is cheaper than Robot with ID 21.", res)

    def test__gt__robots_are_equal(self):
        r1 = Robot("12", "Education", 10, 99.99)
        r2 = Robot("21", "Entertainment", 10, 99.99)

        res = r1 > r2

        self.assertEqual("Robot with ID 12 costs equal to Robot with ID 21.", res)


if __name__ == '__main__':
    main()
