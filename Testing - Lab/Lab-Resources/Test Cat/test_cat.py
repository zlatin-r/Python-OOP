from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_correct_init(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_if_is_fed_expected_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))
    #
    # def test_eat_if_is_not_fed(self):

if __name__ == '__main__':
    main()
