from project.clients.base_client import BaseClient


class RegularClient(BaseClient):

    def __init__(self, name):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount: float):
        points_earned = order_amount // 10
        self.points += points_earned
        return points_earned
