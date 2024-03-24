from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_correct_init(self):
        self.assertEqual(self.cat.name, "Tom")

    def test_eat_if_is_fed_expected_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(str(ex.exception), "Already fed.")


if __name__ == '__main__':
    main()
