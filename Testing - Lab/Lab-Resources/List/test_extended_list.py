from unittest import TestCase, main

from extended_list import IntegerList


class TestExtendedList(TestCase):
    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init_ignores_non_integer_values(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())


if __name__ == '__main__':
    main()
