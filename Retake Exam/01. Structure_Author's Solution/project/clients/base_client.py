from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in ["Regular", "VIP"]:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, amount: float):
        pass

    def apply_discount(self):
        discount_percentage = 0

        if self.points >= 100:
            discount_percentage = 10
            self.points -= 100
        elif 50 <= self.points < 100:
            discount_percentage = 5
            self.points -= 50

        return discount_percentage, self.points
