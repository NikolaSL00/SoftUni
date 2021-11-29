# from project.animal import Animal
# from project.caretaker import Caretaker
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.lion import Lion
# from project.tiger import Tiger
# from project.vet import Vet
# from project.worker import Worker
from project import *


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return f"Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = sum([x.salary for x in self.workers])

        if self.__budget < sum_of_salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_of_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_of_animals_care = sum([x.money_for_care for x in self.animals])

        if self.__budget < sum_of_animals_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum_of_animals_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        tigers = [x for x in self.animals if x.__class__.__name__ == "Tiger"]
        cheetahs = [x for x in self.animals if x.__class__.__name__ == "Cheetah"]

        result_message = f"You have {len(self.animals)} animals"

        result_message += self.all_animals_of_type(lions, "Lions")
        result_message += self.all_animals_of_type(tigers, "Tigers")
        result_message += self.all_animals_of_type(cheetahs, "Cheetahs")

        return result_message

    def all_animals_of_type(self, list_of_animals, type_name):

        result_message = f"\n----- {len(list_of_animals)} {type_name}:"
        for animal in list_of_animals:
            result_message += f"\n{animal.__repr__()}"
        return result_message

    def workers_status(self):
        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]
        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]

        result_message = f"You have {len(self.workers)} workers"

        result_message += self.all_workers_of_type(keepers, "Keepers")
        result_message += self.all_workers_of_type(caretakers, "Caretakers")
        result_message += self.all_workers_of_type(vets, "Vets")

        return result_message

    def all_workers_of_type(self, list_of_workers, type_name):

        result_message = f"\n----- {len(list_of_workers)} {type_name}:"
        for worker in list_of_workers:
            result_message += f"\n{worker.__repr__()}"
        return result_message
