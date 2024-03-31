from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShopping(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Metro", 100.00)

    def test_init(self):
        self.assertEqual("Metro", self.cart.shop_name)
        self.assertEqual(100.00, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_setter_name_invalid_value_contains_digit_returns_value_error(self):
        expect = "Shop must contain only letters and must start with capital letter!"

        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Sho3p"

        self.assertEqual(expect, str(ve.exception))

    def test_setter_name_invalid_value_starts_with_lowercase_returns_value_error(self):
        expect = "Shop must contain only letters and must start with capital letter!"

        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "shop"

        self.assertEqual(expect, str(ve.exception))

    def test_add_to_cart_product_to_expensive_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Monitor", 100)

        self.assertEqual("Product Monitor cost too much!", str(ve.exception))

    def test_add_to_cart_happy_case(self):
        res = self.cart.add_to_cart("Monitor", 99.9)

        expected_message = f"Monitor product was successfully added to the cart!"

        self.assertEqual({"Monitor": 99.9}, self.cart.products)
        self.assertEqual(expected_message, res)

    def test_remove_from_cart_no_such_product_in_cart_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Monitor")

        self.assertEqual("No product with name Monitor in the cart!", str(ve.exception))

    def test_remove_from_cart_happy_case(self):
        self.cart.products = {"Monitor": 99.9}

        res = self.cart.remove_from_cart("Monitor")
        expected_message = "Product Monitor was successfully removed from the cart!"

        self.assertEqual(expected_message, res)
        self.assertEqual({}, self.cart.products)


if __name__ == "__main__":
    main()
