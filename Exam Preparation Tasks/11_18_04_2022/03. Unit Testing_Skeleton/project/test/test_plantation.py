from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_correct_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_invalid_value_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_but_already_hired_raise_exception(self):
        self.plantation.workers = ["Worker"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Worker")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_happy_case(self):
        res = self.plantation.hire_worker("Worker")

        self.assertEqual("Worker successfully hired.", res)
        self.assertEqual(["Worker"], self.plantation.workers)

    def test__len__(self):
        self.plantation.plants = {"Iva": ["flower", "shroom"]}
        self.assertEqual(2, len(self.plantation))

    def test_planting_worker_not_in_workers_raises_error(self):
        self.plantation.workers = []
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Jack", "rose")

        self.assertEqual("Worker with name Jack is not hired!", str(ve.exception))

    def test_planting_plantation_is_full_raises_exception(self):
        self.plantation.size = 1
        self.plantation.workers = ["Jim", "Sam"]
        self.plantation.planting("Jim", "tulips")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Sam", "roses")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_worker_has_already_planted_plans(self):
        self.plantation.workers = ["John"]
        self.plantation.plants = {"John": ["Tulips"]}
        res = self.plantation.planting("John", "Roses")

        self.assertEqual("John planted Roses.", res)
        self.assertEqual({"John": ["Tulips", "Roses"]}, self.plantation.plants)

    def test_planting_worker_has_no_planted_plans(self):
        self.plantation.workers = ["John"]
        res = self.plantation.planting("John", "Roses")

        self.assertEqual({"John": ["Roses"]}, self.plantation.plants)
        self.assertEqual("John planted it's first Roses.", res)

    def test__str__(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "Grape")

        expect = "Plantation size: 10\nIvan\nIvan planted: Grape"
        result = str(self.plantation)

        self.assertEqual(expect, result)

    def test__repr__(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "Grape")

        expect = "Size: 10\nWorkers: Ivan"
        result = str(self.plantation.__repr__())

        self.assertEqual(expect, result)



if __name__ == '__main__':
    main()
