from project.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow meow!"

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {animal_type}"
