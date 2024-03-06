from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int) -> str:

        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:

        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):

        try:
            name = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(name)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_needed = sum([a.money_for_care for a in self.animals])

        if total_money_needed <= self.__budget:
            self.__budget -= total_money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_status = f"You have {len(self.animals)} animals\n"
        dict_animals = {"Lion": [], "Tiger": [], "Cheetah": []}

        for animal in self.animals:
            animal_class = animal.__class__.__name__
            dict_animals[animal_class].append(animal)

        for species in dict_animals.keys():
            animals_status += f"----- {len(dict_animals.get(species))} {species}s:\n"

            for data in dict_animals.get(species):
                animals_status += f"{data}\n"

        return animals_status.strip()

    def workers_status(self):
        workers_status = f"You have {len(self.workers)} workers\n"
        dict_workers = {"Keeper": [], "Caretaker": [], "Vet": []}

        for worker in self.workers:
            worker_class = worker.__class__.__name__
            dict_workers[worker_class].append(worker)

        for work in dict_workers.keys():
            workers_status += f"----- {len(dict_workers.get(work))} {work}s:\n"

            for data in dict_workers.get(work):
                workers_status += f"{data}\n"

        return workers_status.strip()
