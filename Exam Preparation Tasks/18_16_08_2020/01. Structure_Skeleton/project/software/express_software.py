from project.software.software import Software


class ExpressSoftware(Software):
    __MEMORY_CONSUMPTION_consumption = 2
    __TYPE = "Express"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, ExpressSoftware.__TYPE, capacity_consumption,
                         int(memory_consumption * ExpressSoftware.__MEMORY_CONSUMPTION_consumption))
