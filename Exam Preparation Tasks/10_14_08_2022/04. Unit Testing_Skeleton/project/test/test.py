from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_with_value_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ve.exception))

    def test__len__returns_total_books_in_store(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 2, "Book2": 3, "Book3": 5}

        self.assertEqual(10, len(self.bookstore))

    def test_receive_book_if_not_enough_space_in_store_raise_exception(self):
        self.bookstore.books_limit = 1
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Book", 2)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_happy_case_book_not_in_store_returns_string_message(self):
        res = self.bookstore.receive_book("Book", 2)

        self.assertEqual({"Book": 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("2 copies of Book are available in the bookstore.", res)
        self.assertEqual(2, len(self.bookstore))

    def test_sell_book_if_book_is_not_available_in_store_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Book", 1)

        self.assertEqual("Book Book doesn't exist!", str(ex.exception))

    def test_sell_book_if_not_enough_copies_available_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book": 1}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Book", 2)

        self.assertEqual("Book has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book_happy_case_books_left_returns_string_message(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book": 5}

        res = self.bookstore.sell_book("Book", 2)

        self.assertEqual("Sold 2 copies of Book", res)
        self.assertEqual({"Book": 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, len(self.bookstore))

    def test_sell_book_happy_case_no_books_left_returns_string_message(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book": 5}

        res = self.bookstore.sell_book("Book", 5)

        self.assertEqual("Sold 5 copies of Book", res)
        self.assertEqual({'Book': 0}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, self.bookstore.total_sold_books)
        self.assertEqual(0, len(self.bookstore))

    def test__str__(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book": 4, "Book1": 3}
        self.bookstore.sell_book("Book", 2)

        result = self.bookstore.__str__()
        expect = "Total sold books: 2\nCurrent availability: 5\n - Book: 2 copies\n - Book1: 3 copies"

        self.assertEqual(expect, result)
        self.assertEqual(5, len(self.bookstore))


if __name__ == '__main__':
    main()
