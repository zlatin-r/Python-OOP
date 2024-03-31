from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShopping(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Metro", 100.00)

    def test_init(self):
        self.assertEqual("Metro", self.cart.shop_name)
        self.assertEqual(100.00, self.cart.budget)
        self.assertEqual({}, self.cart.products)


if __name__ == "__main__":
    main()
