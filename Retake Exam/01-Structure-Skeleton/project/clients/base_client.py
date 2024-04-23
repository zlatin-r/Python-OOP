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
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        if self.points >= 100:
            self.points -= 100
            return (10, self.points)

        elif 50 <= self.points < 100:
            self.points -= 50
            return (50, self.points)

        else:
            return (0, self.points)
            # TODO CHECK 0 DISCOUNT
