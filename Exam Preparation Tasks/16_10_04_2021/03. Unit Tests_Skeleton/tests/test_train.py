from unittest import TestCase, main
from project.railway_station import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Test", 100)

    def test_correct_init(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_when_train_is_full_raises_value_error(self):
        self.train.capacity = 1
        self.train.passengers = ["Ivan"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Gosho")

        self.assertEqual("Train is full", str(ve.exception))

    def test_add_passenger_when_passenger_already_added_raises_value_error(self):
        self.train.capacity = 5
        self.train.passengers = ["Ivan"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Ivan")

        self.assertEqual("Passenger Ivan Exists", str(ve.exception))

    def test_add_passenger_happy_case(self):
        res = self.train.add("Ivan")

        self.assertEqual("Added passenger Ivan", res)
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual(["Ivan"], self.train.passengers)

    def test_remove_passenger_but_passenger_not_found_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Ivan")

        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual(0, len(self.train.passengers))
        self.assertEqual([], self.train.passengers)

    def test_remove_passenger_happy_case(self):
        self.train.passengers = ["Ivan", "Gosho"]
        res = self.train.remove("Ivan")

        self.assertEqual("Removed Ivan", res)
        self.assertEqual(["Gosho"], self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))


if __name__ == '__main__':
    main()
