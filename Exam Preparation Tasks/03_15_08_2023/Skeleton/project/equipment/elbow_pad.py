from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25.0
    INCREASE_FACTOR = 0.10

    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    def increase_price(self):
        self.PRICE += self.PRICE * self.INCREASE_FACTOR
