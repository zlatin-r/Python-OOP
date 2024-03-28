from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    MEALS = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu = []
        self.clients = []

    def register_client(self, client_phone_number: str):
        if self._find_client_by_phone_number(client_phone_number):
            raise Exception("The client has already been registered!")
        self.clients.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.MEALS:
                self.menu.append(meal)

    def show_menu(self):
        self._check_if_menu_is_ready()

        result = []
        for meal in self.menu:
            result.append(meal.details())
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._check_if_menu_is_ready()

        if not self._find_client_by_phone_number(client_phone_number):
            self.clients.append(Client(client_phone_number))

        for meal_name, quantity in meal_names_and_quantities.items():
            menu_meal = self._find_meal_in_menu_by_name(meal_name)

            if not menu_meal:
                raise Exception(f"{meal_name} is not on the menu!")

            if quantity > menu_meal.quantity:
                raise Exception(f"Not enough quantity of {menu_meal.__class__.__name__}: {meal_name}!")


    # Helping methods



    def _find_meal_in_menu_by_name(self,meal_name: str):
        meal = next(filter(lambda  m: m.name == meal_name, self.menu), None)
        return meal

    def _find_client_by_phone_number(self, phone_number: str):
        client = next(filter(lambda c: c.phone_number == phone_number, self.clients), None)
        return client

    def _check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
