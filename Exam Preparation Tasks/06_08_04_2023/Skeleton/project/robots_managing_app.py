from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")
        new_service = self.VALID_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._find_robot_by_name(robot_name)
        service = self._find_service_by_name(service_name)
        if robot.SERVICE != service.ROBOT_NEEDED:
            return "Unsuitable service."
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._find_service_by_name(service_name)
        robot = self._find_robot_in_service(robot_name, service)
        if not robot:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._find_service_by_name(service_name)
        robots = len([r.eating() for r in service.robots])
        return f"Robots fed: {robots}."

    def service_price(self, service_name: str):
        service = self._find_service_by_name(service_name)
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    def _find_robot_in_service(self, robot_name: str, service: BaseService):
        return next(filter(lambda r: r.name == robot_name, service.robots), None)

    def _find_robot_by_name(self, robot_name: str):
        return next(filter(lambda r: r.name == robot_name, self.robots), None)

    def _find_service_by_name(self, service_name: str):
        return next(filter(lambda s: s.name == service_name, self.services), None)
