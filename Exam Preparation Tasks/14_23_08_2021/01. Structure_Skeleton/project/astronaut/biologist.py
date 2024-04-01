from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, Biologist.INITIAL_OXYGEN)

    @property
    def breath_unit(self):
        return 5

    def breathe(self):
        self.oxygen -= self.breath_unit

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount
