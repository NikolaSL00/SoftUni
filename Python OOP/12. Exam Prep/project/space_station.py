from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.__create_astronaut(astronaut_type, name)
        self.astronaut_repository.astronauts.append(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {name} was retired!"

        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception(f"Invalid planet name!")

        suitable_astronauts = self.astronaut_repository.find_suitable_astronauts_for_mission(5, 30)
        if len(suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        participated_astronauts = 0
        for astronaut in suitable_astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1

        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {participated_astronauts} astronauts participated in collecting items."
        self.failed_missions += 1
        return f"Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n" \
                 f"{self.failed_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut)
        return result.strip()

    @staticmethod
    def __create_astronaut(astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        elif astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        elif astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")
