from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_correct_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)


if __name__ == '__main__':
    main()
