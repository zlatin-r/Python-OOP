from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        self._find_delicacy_by_name_and_return(name, self.delicacies)
        if type_delicacy not in self.DELICACY_TYPES:
            raise ValueError(f"{type_delicacy} is not on our delicacy menu!")
        new_delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        self._find_booth_by_number_and_return(booth_number, self.booths)
        if type_booth not in self.BOOTH_TYPES:
            raise ValueError(f"{type_booth} is not a valid booth!")
        new_booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        free_booths = [b for b in self.booths if b.is_reserved is False]
        booth = next(filter(lambda b: b.capacity >= number_of_people, free_booths), None)
        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        both = self._find_booth_by_number(booth_number)
        if not both:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy = next(filter(lambda c: c.name == delicacy_name, self.delicacies), None)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        both.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._find_booth_by_number(booth_number)
        bill = sum([b.price for b in booth.delicacy_orders]) + booth.price_for_reservation
        self.income += bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    #  HELPING METHODS:

    def _find_booth_by_number(self, booth_number: int):
        return next(filter(lambda b: b.booth_number == booth_number, self.booths), None)

    def _find_delicacy_by_name_and_return(self, name: str, collection: list):
        result = next(filter(lambda d: d.name == name, collection), None)
        if result:
            raise Exception(f"{name} already exists!")
        return result

    def _find_booth_by_number_and_return(self, booth_number: int, collection: list):
        result = next(filter(lambda b: b.booth_number == booth_number, collection), None)
        if result:
            raise Exception(f"Booth number {booth_number} already exists!")
        return result
