from project.toy_store import ToyStore
import unittest


class TestToyStoreClass(unittest.TestCase):
    def test_correct_init(self):
        self.toy_store = ToyStore()
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_method_shelf_not_in_store(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("K", "ToyTestName")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_method_toy_already_in_shelf(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("D", "ToyTestName")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("D", "ToyTestName")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_method_shelf_is_already_taken(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("D", "ToyTestNameOne")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("D", "ToyTestNameTwo")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_method_successfully_added_toy_on_shelf(self):
        self.toy_store = ToyStore()
        result = self.toy_store.add_toy("A", "ToyTestName")

        self.assertEqual(result, "Toy:ToyTestName placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "ToyTestName",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_remove_toy_method_shelf_is_already_taken(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("K", "ToyTestName")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_method_toy_on_that_shelf_does_not_exist(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "ToyTestName")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

        self.toy_store.add_toy("A", "ToyTestNameOne")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "ToyTestNameTwo")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_method_successfully_removed_toy_from_shelf(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "ToyTestName")
        result = self.toy_store.remove_toy("A", "ToyTestName")

        self.assertEqual(result, "Remove toy:ToyTestName successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })


if __name__ == '__main__':
    unittest.main()
