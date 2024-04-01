from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    __CAPACITY = 0.25
    __MEMORY = 1.75
    __TYPE = "Power"

    def __init__(self, name, capacity, memory):
        super().__init__(name, self.__TYPE, int(capacity * self.__CAPACITY), int(memory * self.__MEMORY))
