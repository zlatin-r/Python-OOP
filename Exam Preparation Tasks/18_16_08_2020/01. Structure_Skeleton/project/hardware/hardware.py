from typing import List
from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = int(capacity)
        self.memory = memory
        self.software_components: List = [Software]

    def install(self, software: Software):
        if software.capacity_consumption <= self.capacity and software.memory_consumption <= self.memory:
            self.capacity -= software.capacity_consumption
            self.memory -= software
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)
