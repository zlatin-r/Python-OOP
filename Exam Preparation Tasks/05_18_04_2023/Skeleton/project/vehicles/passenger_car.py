from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_milеage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduce_percentage = int((mileage / self.MAX_MILEAGE) * 100)
        self.MAX_MILEAGE -= mileage
        self.battery_level *= reduce_percentage  # TODO CHECK THE RESULT
