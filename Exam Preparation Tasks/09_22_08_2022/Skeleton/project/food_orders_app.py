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


    # Helping functions



