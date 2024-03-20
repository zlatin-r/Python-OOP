from abc import ABC, abstractmethod


class BaseService(ABC):

    ERROR_MSG_NAME = "Service name cannot be empty!"
    ERROR_MSG_CAPACITY = "Service capacity cannot be less than or equal to 0!"

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @abstractmethod
    def details(self):
        pass

    def _get_names(self):
        if not self.robots:
            return "none"
        return " ".join([r.name for r in self.robots])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_NAME)
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(self.ERROR_MSG_CAPACITY)
        self.__capacity = value
