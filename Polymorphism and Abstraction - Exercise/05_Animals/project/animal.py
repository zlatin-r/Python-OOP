from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age
    
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass
