from typing import List

from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List = [Booth]
        self.delicacies: List = [Delicacy]
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        pass

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
