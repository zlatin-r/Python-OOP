from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    STOLEN_PORTION = 250

    def __init__(self, name, price):
        super().__init__(name, self.STOLEN_PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
