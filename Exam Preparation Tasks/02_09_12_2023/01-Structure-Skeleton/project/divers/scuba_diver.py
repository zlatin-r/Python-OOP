from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXY_LEVEL = 540

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXY_LEVEL)

    def miss(self, time_to_catch: int):
        reduce_value = time_to_catch * 0.30
        if self.oxygen_level < reduce_value:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduce_value
        round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXY_LEVEL
