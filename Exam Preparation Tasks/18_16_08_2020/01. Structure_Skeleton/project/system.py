from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    def register_power_hardware(self, name: str, capacity: int, memory: int):
        item = PowerHardware(name, capacity, memory)
        self._hardware.append(item)

    def register_heavy_hardware(self, name: str, capacity: int, memory: int):
        item = HeavyHardware(name, capacity, memory)
        self._hardware.append(item)

    def register_express_software(self, hardware_name: str, name: str,
                                  capacity_consumption: int, memory_consumption: int):
        hardware = next(filter(lambda item: item.name == hardware_name, self._hardware), None)

        if not hardware:
            return "Hardware does not exist"

        software = ExpressSoftware(capacity_consumption, memory_consumption)
        hardware.install(software)
