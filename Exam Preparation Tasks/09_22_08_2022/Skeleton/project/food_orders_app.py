from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    MEALS = ["Starter", "MainDish", "Dessert"]
    def __init__(self):
        self.menu = []
        self.clients_list = []


    def register_client(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)
        if client:
            self.clients_list.append(client)
            return f"Client {client_phone_number} registered successfully."
        else:
            raise Exception("The client has already been registered!")

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if not self._check_is_menu_ready(self.menu):
            raise Exception("The menu is not ready!")
        return "\n".join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        meals, bill = [], 0.0
        client = self._find_client_by_phone_number(client_phone_number)

        if self._check_is_menu_ready(self.menu):
            if not client:
                new_client = Client(client_phone_number)
                self.clients_list.append(new_client)
            for m, q in meal_names_and_quantities.items():
                if self._check_is_meal_in_menu(m):
                    meal = self._find_meal_by_name(m)
                    if self._check_quantity(meal, q):
                        meal.quantity -= q
                        meals.append(meal)
                        bill += q * meal.price
                    else:
                        meals, bill = [], 0.0
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {m}!")
                else:
                    meals, bill = [], 0.0
                    raise Exception("{meal_name} is not on the menu!")
        else:
            meals, bill = [], 0.0
            raise Exception("The menu is not ready!")

        client.shopping_cart.extend(meals)
        client.bill += bill

    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)
        client.shopping_cart = []



    # helping methods:

    def _find_client_by_phone_number(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        return client

    def _find_meal_by_name(self, meal_name: str):
        return next(filter(lambda m: m.name == meal_name, self.menu))

    def _check_is_menu_ready(self, menu):
        return len(menu) >= 5

    def _check_is_meal_in_menu(self, meal_name):
        meal = next(filter(lambda m: m.name == meal_name, self.menu), None)
        if meal:
            return True
        return False

    def _check_quantity(self, meal, quantity):
        return meal.quantity >= quantity

    def _return_products_to_menu(self, shopping_cart):
        for product in shopping_cart:
            self

