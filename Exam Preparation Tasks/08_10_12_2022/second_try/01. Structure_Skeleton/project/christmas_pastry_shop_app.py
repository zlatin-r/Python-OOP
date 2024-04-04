from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
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
        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        try:
            b = [b for b in self.booths if b.booth_number == booth_number][0]
            raise Exception(f"Booth number {booth_number} already exists!")
        except IndexError:
            new_booth = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
            self.booths.append(new_booth)
            return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        try:
            booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved][0]
            booth.reserve(number_of_people)
            return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        except IndexError:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths), None)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies), None)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        total_bill = sum([d.price for d in booth.delicacy_orders]) + booth.price_for_reservation

        booth.delicacy_orders = []
        booth.price_for_reservation = 0.0
        booth.is_reserved = False

        self.income += total_bill
        return f"Booth {booth_number}:\nBill: {total_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
