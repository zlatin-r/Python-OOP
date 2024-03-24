from unittest import TestCase, main

from extended_list import IntegerList


class TestExtendedList(TestCase):
    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init_ignores_non_integer_values(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_add_non_integer_elements_to_the_list_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))


if __name__ == '__main__':
    main()
