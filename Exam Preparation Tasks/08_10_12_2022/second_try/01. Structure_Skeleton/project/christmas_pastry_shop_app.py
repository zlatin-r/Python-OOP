from typing import List

from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_ID_NUMBER = 0

    def __init__(self):
        self.booths: List = [Booth]
        self.delicacies: List = [Delicacy]
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.VALID_DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        try:
            d = [d for d in self.delicacies if d.name == name][0]
            raise Exception(f"{name} already exists!")
        except IndexError:
            new_delicacy = self.VALID_DELICACY_TYPES[type_delicacy](name, price)
            self.delicacies.append(new_delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        pass

    def reserve_booth(self, number_of_people: int):
        pass

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        pass

    def leave_booth(self, booth_number: int):
        pass

    def get_income(self):
        pass
