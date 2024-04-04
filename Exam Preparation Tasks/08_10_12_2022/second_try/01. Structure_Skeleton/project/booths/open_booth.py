from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PRO_PERSON = 2.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.PRICE_PRO_PERSON
        self.is_reserved = True
