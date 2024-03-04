from project import worker
from project.worker import Worker
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet
from project.animal import Animal
from project.lion import Lion
from project.cheetah import Cheetah
from project.tiger import Tiger


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Lion or Cheetah or Tiger, price):
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity <= 0:
            return "Not enough space for animal"

        self.__budget -= price
        self.__animal_capacity -= 1
        self.animals.append(animal)
        class_name = type(animal).__name__
        return f"{animal.name} the {class_name} added to the zoo"

    def hire_worker(self, worker: Keeper or Vet or Caretaker):
        if self.__workers_capacity <= 0:
            return "Not enough space for worker"

        self.__workers_capacity -= 1
        self.workers.append(worker)
        class_name = type(worker).__name__
        return f"{worker.name} the {class_name} hired successfully"

    def fire_worker(self, worker_name: str):

        try:
            name = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(name)
        self.__workers_capacity -= 1
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_salaries = sum(list(map(lambda w: w.salary, self.workers)))
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_needed = sum(list(map(lambda w: w.money_for_care, self.animals)))
        if total_money_needed <= self.__budget:
            self.__budget -= total_money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_status = ""
        animals_status += f"You have {len(self.animals)} animals\n"

        dict_animals = {}

        for animal in self.animals:
            animal_class = type(animal).__name__
            if animal_class not in dict_animals.keys():
                dict_animals[animal_class] = []
            dict_animals[animal_class].append(animal)

        species_order = ["Lion", "Tiger", "Cheetah"]

        for species in species_order:
            animals_list = dict_animals.get(species)
            animals_status += f"----- {len(animals_list)} {species}s:\n"
            for data in animals_list:
                animals_status += f"{data}\n"

        return animals_status.strip()

    def workers_status(self):
        workers_status = ""
        workers_status += f"You have {len(self.animals)} animals\n"

        dict_workers = {}

        for worker in self.workers:
            worker_class = type(worker).__name__
            if worker_class not in dict_workers.keys():
                dict_workers[worker_class] = []
            dict_workers[worker_class].append(worker)

        workers_order = ["Keeper", "Caretaker", "Vet"]

        for work in workers_order:
            workers_list = dict_workers.get(work)
            workers_status += f"----- {len(workers_list)} {work}s:\n"
            for data in workers_list:
                workers_status += f"{data}\n"

        return workers_status.strip()
