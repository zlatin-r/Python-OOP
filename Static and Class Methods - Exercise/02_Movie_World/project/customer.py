class Customer:

    def __init__(self, name: str, age: int, _id: int):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds = []

    def __repr__(self):
        return (f"{id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({', '.join(self.rented_dvds)})")
