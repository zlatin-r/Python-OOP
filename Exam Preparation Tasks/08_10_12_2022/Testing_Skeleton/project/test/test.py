from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_init(self):
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_shelf_not_in_store_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("X", "ball")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_the_toy_is_already_on_shelf_raises_exception(self):
        self.toy_store.add_toy("A", "doll")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "doll")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_to_a_taken_shelf_raises_exception(self):
        self.toy_store.add_toy("G", "toy")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("G", "car")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_happy_case(self):
        res = self.toy_store.add_toy("F", "sword")

        self.assertEqual("Toy:sword placed successfully!", res)

    def test_remove_toy_from_invalid_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "teddy bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_the_toy_name_is_invalid_raises_exception(self):
        self.toy_store.add_toy("F", "ball")

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("F", "doll")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_happy_case(self):
        self.toy_store.add_toy("E", "rocket")

        res = self.toy_store.remove_toy("E", "rocket")

        self.assertEqual("Remove toy:rocket successfully!", res)
        self.assertEqual(None, self.toy_store.toy_shelf["E"])


if __name__ == '__main__':
    main()
