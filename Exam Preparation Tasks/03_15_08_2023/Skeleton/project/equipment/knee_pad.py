from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    PRICE = 15.0
    INCREASE_FACTOR = 0.20

    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    def increase_price(self):
        self.PRICE += self.PRICE * self.INCREASE_FACTOR
