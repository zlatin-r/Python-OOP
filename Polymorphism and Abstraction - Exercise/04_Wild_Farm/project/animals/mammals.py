from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog:
    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat:
    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger:
    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
