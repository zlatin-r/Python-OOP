from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90

    def __init__(self, name):
        super().__init__(name, Meteorologist.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= 15

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount
