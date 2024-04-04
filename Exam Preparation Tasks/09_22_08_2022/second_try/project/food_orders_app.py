from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEAL_TYPES = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    RECEIPT_ID = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):

        try:
            cl = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
            raise Exception("The client has already been registered!")
        except IndexError:
            new_client = Client(client_phone_number)
            self.clients_list.append(new_client)
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in self.VALID_MEAL_TYPES:
                self.menu.append(meal)

    def show_menu(self):
        self._validate_menu()

        return "\n".join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._validate_menu()
        client = self._validate_client(client_phone_number)

        current_order = []
        current_bill = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == meal_name, self.menu), None)

            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")

            meal.quantity -= quantity
            ordered_meal = self.VALID_MEAL_TYPES[type(meal).__name__](meal.name, meal.price, quantity)
            current_order.append(ordered_meal)
            current_bill += ordered_meal.price * quantity

        client.shopping_cart.extend(current_order)
        client.bill += current_bill
        return (f"Client {client_phone_number} successfully ordered "
                f"{', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = self._validate_client(client_phone_number)

        if client.shopping_cart:
            for meal in client.shopping_cart:
                menu_meal = next(filter(lambda m: m.name == meal.name, self.menu))
                menu_meal.quantity += meal.quantity
            client.shopping_cart = []
            client.bill = 0.0
            return f"Client {client_phone_number} successfully canceled his order."
        else:
            raise Exception("There are no ordered meals!")

    def finish_order(self, client_phone_number: str):
        client = self._validate_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.RECEIPT_ID += 1
        client.shopping_cart = []
        final_bill = client.bill
        client.bill = 0.0

        return (f"Receipt #{self.RECEIPT_ID} with total amount of {final_bill:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    # HELPING METHODS:

    def _validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def _validate_client(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        if not client:
            self.clients_list.append(Client(client_phone_number))
        return client
