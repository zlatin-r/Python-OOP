from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    MEALS = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        if not client:
            self.clients_list.append(Client(client_phone_number))
            return f"Client {client_phone_number} registered successfully."
        else:
            raise Exception("The client has already been registered!")

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.MEALS:
                self.menu.append(meal)

    def show_menu(self):
        self._check_if_menu_is_ready()
        menu_details = []
        for meal in self.menu:
            menu_details.append(meal.details())
        return "\n".join(menu_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._check_if_menu_is_ready()
        client = self._find_client_by_phone_number(client_phone_number)

    # Helping functions

    def _check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def _find_client_by_phone_number(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        if not client:
            self.clients_list.append(Client(client_phone_number))
        return client