from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if self._find_client_by_phone_number(client_phone_number):
            raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
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

        client = self._find_client_by_phone_number(client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for meal_name, quantity in meal_names_and_quantities.items():
            menu_meal = self._find_meal_in_menu_by_name(meal_name)

            if not menu_meal:
                raise Exception(f"{meal_name} is not on the menu!")

            if quantity > menu_meal.quantity:
                raise Exception(f"Not enough quantity of {menu_meal.__class__.__name__}: {meal_name}!")

            menu_meal.quantity -= quantity
            order = self.MEALS[menu_meal.__class__.__name__](meal_name, menu_meal.price, quantity)
            client.shopping_cart.append(order)

            client.bill += order.quantity * order.price

        ordered_meal_names = [m.name for m in client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered {', '.join(ordered_meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, phone_number: str):
        client = self._find_client_by_phone_number(phone_number)

        if client.shopping_cart:
            for meal in client.shopping_cart:
                for menu_meal in self.menu:
                    if meal.name == menu_meal.name:
                        client.bill -= meal.price * meal.quantity
                        menu_meal.quantity += meal.quantity
                        client.shopping_cart.remove(meal)
            client.orders = {}
            return f"Client {phone_number} successfully canceled his order."
        raise Exception("There are no ordered meals!")

    def finish_order(self, phone_number: str):
        self.RECEIPT_ID += 1
        client = self._find_client_by_phone_number(phone_number)
        if client.shopping_cart:
            return (f"Receipt #{self.RECEIPT_ID} with total amount of "
                    f"{client.bill:.2f} was successfully paid for {phone_number}.")
        raise Exception("There are no ordered meals!")

    def __str__(self):
        return (f"Food Orders App has {len(self.menu)} "
                f"meals on the menu and {len(self.clients_list)} clients.")

    # Helping methods
    def _find_meal_in_menu_by_name(self, meal_name: str):
        meal = next(filter(lambda m: m.name == meal_name, self.menu), None)
        return meal

    def _find_client_by_phone_number(self, phone_number: str):
        client = next(filter(lambda c: c.phone_number == phone_number, self.clients_list), None)
        return client

    def _check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")