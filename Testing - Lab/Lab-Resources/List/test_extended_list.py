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

    def test_add_integer_to_the_list(self):
        expected_list = self.i_list.get_data() + [4]

        self.i_list.add(4)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_element_on_out_of_range_index_expected_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_element_from_list_whit_valid_index(self):
        expected_result = [1, 3]

        self.i_list.remove_index(1)

        self.assertEqual(expected_result, self.i_list.get_data())

    def test_get_element_from_list_on_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_element_from_the_list_on_valid_index(self):
        result = self.i_list.get(1)

        self.assertEqual(2, result)



if __name__ == '__main__':
    main()
