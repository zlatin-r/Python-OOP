from project.meals.meal import Meal


class Dessert(Meal):
    INITIAL_QUANTITY = 30

    def __init__(self, name: str, price: float):
        super().__init__(name, price, self.INITIAL_QUANTITY)

    def details(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"
