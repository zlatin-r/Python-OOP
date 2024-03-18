from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PRICE = 15.0
    PROTECTION = 120
    TYPE_ = "KneePad"

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= 1.20
