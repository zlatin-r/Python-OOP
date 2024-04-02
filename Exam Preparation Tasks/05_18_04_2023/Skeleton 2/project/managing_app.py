from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
    ROADS_COUNT = 0

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            next(filter(lambda usr: usr.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            next(filter(lambda vhc: vhc.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            self.vehicles.append(self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        self.ROADS_COUNT += 1

        for road in self.routes:
            if road.start_point == start_point and road.end_point == end_point:
                if road.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif road.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                else:
                    road.is_locked = True

        self.routes.append(Route(start_point, end_point, length, self.ROADS_COUNT))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(filter(lambda usr: usr.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda vhc: vhc.license_plate_number == license_plate_number, self.vehicles))
        road = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed"

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if road.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(road.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))[:count]

        for vehicle in vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)

        result = ["*** E-Drive-Rent ***", "\n".join(str(u) for u in sorted_users)]
        return result
