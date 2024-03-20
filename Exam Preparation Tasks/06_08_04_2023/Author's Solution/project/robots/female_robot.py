from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIAL_WEIGHT = 7
    INCREMENT_WEIGHT = 1
    POSSIBLE_SERVICE = 'SecondaryService'

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=self.INITIAL_WEIGHT)

    def eating(self):
        self.weight += self.INCREMENT_WEIGHT