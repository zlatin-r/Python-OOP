from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90

    def __init__(self, name):
        super().__init__(name, Meteorologist.INITIAL_OXYGEN)

    @property
    def breath_unit(self):
        return 15

    def breathe(self):
        self.oxygen -= self.breath_unit

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount
