from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        self.battery_level -= round(mileage / self.MAX_MILEAGE * 100)
