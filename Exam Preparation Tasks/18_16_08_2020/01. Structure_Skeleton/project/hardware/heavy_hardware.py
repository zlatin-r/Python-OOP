from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    __CAPACITY = 2
    __MEMORY = 0.75
    __TYPE = "Heavy"

    def __init__(self, name, capacity, memory):
        super().__init__(name, self.__TYPE, int(capacity * self.__CAPACITY), int(memory * self.__MEMORY))
