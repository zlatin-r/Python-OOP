from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("TestName", 10)

    def test_correct_init(self):
        self.assertEqual(self.restaurant.name, "TestName")
        self.assertEqual(self.restaurant.capacity, 10)
        self.assertEqual(self.restaurant.waiters, [])

    def test_name_setter_with_incorrect_value(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ""

        self.assertEqual(str(ve.exception), "Invalid name!")

    def test_setter_capacity_with_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1

        self.assertEqual(str(ve.exception), "Invalid capacity!")

    def test_get_waiters(self):
        waiter_1 = {"name": "Waiter 1", "total_earnings": 0}
        waiter_2 = {"name": "Waiter 2", "total_earnings": 1}
        waiter_3 = {"name": "Waiter 3", "total_earnings": 2}

        self.restaurant.waiters = [waiter_1, waiter_2, waiter_3]

        self.assertEqual(self.restaurant.waiters, [waiter_1, waiter_2, waiter_3])

        self.assertEqual(self.restaurant.get_waiters(), [waiter_1, waiter_2, waiter_3])
        self.assertEqual(self.restaurant.get_waiters(0, 0), [waiter_1])
        self.assertEqual(self.restaurant.get_waiters(1, 1), [waiter_2])
        self.assertEqual(self.restaurant.get_waiters(2, 2), [waiter_3])
        self.assertEqual(self.restaurant.get_waiters(3), [])
        self.assertEqual(self.restaurant.get_waiters(1, 2), [waiter_2, waiter_3])
        self.assertEqual(self.restaurant.get_waiters(1), [waiter_2, waiter_3])
        self.assertEqual(self.restaurant.get_waiters(2), [waiter_3])
        self.assertEqual(self.restaurant.get_waiters(1, 1), [waiter_2])

    def test_add_waiter_no_capacity(self):
        self.restaurant.capacity = 0
        self.assertEqual(self.restaurant.add_waiter("Jo"), "No more places!")

    def test_add_waiter_name_already_added(self):
        waiter = {"name": "Jo", "total_earnings": 0}
        self.restaurant.waiters = [waiter]
        self.assertEqual(self.restaurant.add_waiter("Jo"), "The waiter Jo already exists!")

    def test_add_waiter_happy_case(self):

        self.assertEqual(self.restaurant.add_waiter("Jo"), "The waiter Jo has been added.")

        self.assertEqual(self.restaurant.waiters, [{"name": "Jo"}])

    def test_remove_waiter_no_name_found(self):
        self.assertEqual(self.restaurant.remove_waiter("Jo"), "No waiter found with the name Jo.")

    def test_remove_waiter_happy_case(self):
        self.restaurant.waiters = [{"name": "Jo", "total_earnings": 0}]

        self.assertEqual(self.restaurant.remove_waiter("Jo"), "The waiter Jo has been removed.")
        self.assertEqual(self.restaurant.waiters, [])

    def test_get_total_earnings(self):
        waiter_1 = {"name": "Waiter 1", "total_earnings": 0}
        waiter_2 = {"name": "Waiter 2", "total_earnings": 1}
        waiter_3 = {"name": "Waiter 3", "total_earnings": 2}

        self.restaurant.waiters = [waiter_1, waiter_2, waiter_3]

        self.assertEqual(self.restaurant.get_total_earnings(), 3)

if __name__ == '__main__':
    main()
