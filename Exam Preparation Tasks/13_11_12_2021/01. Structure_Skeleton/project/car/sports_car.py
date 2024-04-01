from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    def speed_limit_check(self):
        if not self.MIN_SPEED_LIMIT <= self.speed_limit <= self.MAX_SPEED_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between "
                             f"{self.MIN_SPEED_LIMIT} and {self.MAX_SPEED_LIMIT}!")
