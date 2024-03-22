from project.meals.meal import Meal


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


    # helping methods:

    def _find_client_by_phone_number(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        return client
