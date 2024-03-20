from abc import ABC, abstractmethod


class BaseRobot(ABC):
    ERROR_MSG_NAME = "Robot name cannot be empty!"
    ERROR_MSG_KIND = "Robot kind cannot be empty!"
    ERROR_MSG_PRICE = "Robot price cannot be less than or equal to 0.0!"

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @abstractmethod
    def eating(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_NAME)
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_KIND)
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError(self.ERROR_MSG_PRICE)
        self.__price = value
