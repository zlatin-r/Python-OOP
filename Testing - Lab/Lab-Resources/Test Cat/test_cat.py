from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_correct_init(self):
        self.assertEqual(self.cat.name, "Tom")


if __name__ == '__main__':
    main()
