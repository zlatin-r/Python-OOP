from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9
    INCREMENT_WEIGHT = 3
    POSSIBLE_SERVICE = 'MainService'

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=self.INITIAL_WEIGHT)

    def eating(self):
        self.weight += self.INCREMENT_WEIGHT
