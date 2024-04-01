from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OXYGEN = 50

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)

    @property
    def breath_unit(self):
        return 10

    def breathe(self):
        self.oxygen -= self.breath_unit

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount
