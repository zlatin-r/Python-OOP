from project.meals.meal import Meal


class Starter(Meal):
    INITIAL_QUANTITY = 60

    def __init__(self, name: str, price: float):
        super().__init__(name, price, self.INITIAL_QUANTITY)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
