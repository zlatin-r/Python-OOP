from project.meals.meal import Meal


class MainDish(Meal):
    INITIAL_QUANTITY = 50

    def __init__(self, name: str, price: float):
        super().__init__(name, price, self.INITIAL_QUANTITY)

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"
