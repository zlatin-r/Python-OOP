from typing import List


class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, obj):
        return Person(self.name, obj.surname)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:

    def __init__(self, name: str, people: list):
        self.name = name
        self.people: List[Person] = people

    def __len__(self, obj):
        return len(self.people)

    def __add__(self, obj):
        return Group(f"{self.name} {obj.name}", self.people + obj.people)

    def __getitem__(self, index):
        return f"Person {index}: {str(self.people[index])}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"



p1 = Person("John", "Smith")
p2 = Person("Jack", "Dean")
print(p1 + p2)
