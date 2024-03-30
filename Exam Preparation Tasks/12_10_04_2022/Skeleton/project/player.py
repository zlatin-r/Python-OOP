class Player:
    def __init__(self, name: str, age: int, stamina: int):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.players_names = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name not valid!")
        if value in self.players_names:
            raise Exception(f"Name {value} is already used!")
        self.players_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if 0 > value or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value
