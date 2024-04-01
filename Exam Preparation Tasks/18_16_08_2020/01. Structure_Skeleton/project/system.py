from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    def register_power_hardware(self, name: str, capacity: int, memory: int):
        hd = PowerHardware(name, capacity, memory)
        self._hardware.append(hd)

    def register_heavy_hardware(self, name: str, capacity: int, memory: int):
        hd = HeavyHardware(name, capacity, memory)
        self._hardware.append(hd)

    def register_express_software(self, hardware_name: str, name: str,
                                  capacity_consumption: int, memory_consumption: int):
        hd = next(filter(lambda i: i.name == hardware_name, self._hardware), None)

        if not hd:
            return "Hardware does not exist"

        sw = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hd.install(sw)

    def register_light_software(self, hardware_name: str, name: str,
                                capacity_consumption: int, memory_consumption: int):
        hd = next(filter(lambda i: i.name == hardware_name, self._hardware), None)

        if not hd:
            return "Hardware does not exist"

        sw = LightSoftware(name, capacity_consumption, memory_consumption)
        hd.install(sw)

    def release_software_component(self, hardware_name: str, software_name: str):
        hd = next(filter(lambda i: i.name == hardware_name, self._hardware), None)
        sw = next(filter(lambda i: i.name == software_name, self._software), None)

        if not hd or not sw:
            return "Some of the components do not exist"

        hd.uninstall(sw)
        self._software.remove(sw)

    def analyze(self):
        number_of_hardware_components = len(self._hardware)
        number_of_software_components = len(self._software)
        total_sw_mem_consumption = sum(map(lambda x: x.memory_consumption, self._software))
        total_hd_memory = sum(map(lambda x: x.memory, self._hardware))
        total_sw_capacity_consumption = sum(map(lambda x: x.capacity_consumption, self._software))
        total_hd_capacity = sum(map(lambda x: x.capacity, self._hardware))

        result = f"System AnalysisHardware Components: {number_of_hardware_components}\n"
        f"Software Components: {number_of_software_components}\n"
        f"Total Operational Memory: {total_sw_mem_consumption} / {total_hd_memory}\n"
        f"Total Capacity Taken: {total_sw_capacity_consumption} / {total_hd_capacity}"

        return result

    def system_split(self):
        result = []
        for hd in self._hardware:

            light_comps = [c for c in hd.software_components if c.software_type == "Light"]
            memory_used = sum(map(lambda x: x.memory_consumption, hd.software_components))
            capacity_used = sum(map(lambda x: x.capacity_consumption, hd.software_components))
            all_sw_names = [s.name for s in hd.software_components]

            result.append(f"Hardware Component - {hd.name}\n"
                          f"Express Software Components: {len(hd.software_components)}\n"
                          f"Light Software Components: {len(light_comps)}\n"
                          f"Memory Usage: {memory_used} / {hd.memory}\n"
                          f"Capacity Usage: {capacity_used} / {hd.capacity}\n"
                          f"Type: {hd.hardware_type}\n"
                          f"Software Components: {', '.join(all_sw_names) if all_sw_names else 'none'}")

        return result
