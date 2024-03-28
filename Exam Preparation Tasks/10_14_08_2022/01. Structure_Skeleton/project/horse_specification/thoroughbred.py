from project.horse_specification.horse import Horse


class ThoroughBred(Horse):
    MAX_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed += 3
