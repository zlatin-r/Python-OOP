from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.client import Client
from project.meals.starter import Starter


class FoodOrdersApp:
    RECEIPT_ID = 0
    MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

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

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            self._check_if_meal_is_in_menu(meal_name)
            self._check_if_quantity_is_in_menu(meal_name, meal_quantity)

            meal = self._find_meal_by_name(meal_name)

            meal.quantity -= meal_quantity
            ordered_meal = self.MEALS[meal.__class__.__name__](meal.name, meal.price, meal_quantity)

            if self._check_if_meal_is_in_ordered_meals(ordered_meal, client.ordered_meals):
                client.ordered_meals[ordered_meal] = meal_quantity
            client.ordered_meals[ordered_meal] += meal_quantity

        for ordered_meal in client.ordered_meals.keys():
            client.shopping_cart.append(ordered_meal)
            client.orders_price += ordered_meal.price * ordered_meal.quantity
        bill = client.orders_price
        client.bill = bill
        orders = client.shopping_cart
        client.shopping_cart.clear()
        client.orders_price = 0
        return (f"Client {client_phone_number} "
                f"successfully ordered {', '.join(meal.name for meal in orders)} "
                f"for {bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("here are no ordered meals!")

        for ordered_meal, order_quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal.name == menu_meal.name:
                    menu_meal.quantity += order_quantity

        client.shopping_cart.clear()
        client.bill = 0
        client.ordered_meals = {}
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        self.RECEIPT_ID += 1
        total_paid_money = client.bill
        client.bill, client.orders_price, client.shopping_cart, client.ordered_meals = 0, 0, [], {}
        return (f"Receipt #{self.RECEIPT_ID} with total amount of "
                f"{total_paid_money:.2f} was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    # Helping functions

    def _check_if_meal_is_in_ordered_meals(self, meal, ordered_meals):
        result = [m for m in ordered_meals.keys() if m.name == meal.name]
        return len(result) == 0

    def _check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def _find_meal_by_name(self, meal_name: str) -> Meal:
        return next(filter(lambda meal: meal.name == meal_name, self.menu))

    def _find_client_by_phone_number(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        if not client:
            self.clients_list.append(Client(client_phone_number))
        return client

    def _check_if_meal_is_in_menu(self, meal_name: str):
        meal = next(filter(lambda m: m.name == meal_name, self.menu), None)
        if not meal:
            raise Exception(f"{meal_name} is not on the menu!")

    def _check_if_quantity_is_in_menu(self, meal_name: str, quantity: int):
        meal = next(filter(lambda m: m.name == meal_name, self.menu))
        if meal.quantity < quantity:
            raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
