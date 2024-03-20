from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30
    ROBOT_NEEDED = "MainService"
    TYPE_ = "Main Service"

    def __init__(self, name):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        return f"""{self.name} Main Service:
Robots: {self._get_names()}"""
