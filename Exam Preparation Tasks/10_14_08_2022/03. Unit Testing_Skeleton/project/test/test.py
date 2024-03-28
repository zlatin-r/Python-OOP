from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_setter_books_limit_value_equal_to_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test__len__method(self):
        self.bookstore.availability_in_store_by_book_titles = {"b1": 2, "b2": 2, "b3": 2, "b4": 2}

        self.assertEqual(8, len(self.bookstore))

    def test_receive_book_but_not_enough_space_in_store_raises_exception(self):
        self.bookstore.books_limit = 2
        self.bookstore.availability_in_store_by_book_titles = {"b1": 2}

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("b2", 2)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_happy_case(self):

        self.bookstore.receive_book("b1", 3)

        self.assertEqual({"b1": 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, len(self.bookstore))

    def test_receive_book_happy_case_returns_correct_string(self):
        res = self.bookstore.receive_book("b1", 3)
        self.assertEqual(f"3 copies of b1 are available in the bookstore.", res)
        self.assertEqual(3, len(self.bookstore))

    def test_sell_book_if_not_available_in_store_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {"b": 2}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("b2", 1)

        self.assertEqual("Book b2 doesn't exist!", str(ex.exception))

    def test_sell_book_but_not_enough_copies_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {"b": 1}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("b", 2)

        self.assertEqual("b has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book_happy_case(self):
        self.bookstore.availability_in_store_by_book_titles = {"b": 5}

        res = self.bookstore.sell_book("b", 2)

        self.assertEqual({"b": 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual("Sold 2 copies of b", res)
        self.assertEqual(3, len(self.bookstore))

    def test__str__without_any_sold_books_and_none_in_stock(self):
        res = str(self.bookstore)
        self.assertEqual("Total sold books: 0\nCurrent availability: 0", res)

    def test__str__with_sold_books_and_some_in_stock(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {"a": 5, "b": 3}
        bookstore.sell_book("a", 3)

        res = str(bookstore)
        self.assertEqual("Total sold books: 3\nCurrent availability: 5\n"
                         " - a: 2 copies\n - b: 3 copies", res)


if __name__ == '__main__':
    main()
