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
            self.workers.remove(name)
            self.__workers_capacity -= 1
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

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
        status = ""
        status += f"You have {len(self.animals)} animals\n"
        lions = []
        cheetahs = []
        tigers = []

        for animal in self.animals:
            if type(animal) == Lion:
                lions.append(animal)
            elif type(animal) == Cheetah:
                cheetahs.append(animal)
            elif type(animal) == Tiger:
                tigers.append(animal)

        status += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            status += f"{lion}\n"
        status += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            status += f"{tiger}\n"
        status += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            status += f"{cheetah}"

        return status

    def workers_status(self):
        status = ""
        status += f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if type(worker) == Keeper:
                keepers.append(worker)
            elif type(worker) == Caretaker:
                caretakers.append(worker)
            elif type(worker) == Vet:
                vets.append(worker)

        status += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            status += f"{keeper}\n"
        status += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            status += f"{caretaker}\n"
        status += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            status += f"{vet}"

        return status
