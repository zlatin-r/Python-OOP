from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, Biologist.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= 5
