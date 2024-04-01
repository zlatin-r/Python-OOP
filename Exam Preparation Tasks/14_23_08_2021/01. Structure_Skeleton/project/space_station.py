from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}
    successful_missions = 0
    not_successful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.VALID_ASTRONAUT_TYPES.keys():
            raise Exception("Astronaut type is not valid!")

        if self._find_element_by_name(name, self.astronaut_repository.astronauts):
            return f"{name} is already added."

        self.astronaut_repository.add(self.VALID_ASTRONAUT_TYPES[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self._find_element_by_name(name, self.planet_repository.planets):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self._find_element_by_name(name, self.astronaut_repository.astronauts)
        if not astronaut:
            return f"Astronaut {name} doesn't exist!"

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self) -> None:
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        astronauts_participate = 0
        planet = self._find_element_by_name(planet_name, self.planet_repository.planets)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_sorted = sorted(self.astronaut_repository.astronauts, key=lambda a: a.oxygen)[:5]
        astronauts_selected = [a for a in astronauts_sorted if a.oxygen > 30]

        if not astronauts_selected:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts = sorted(astronauts_selected, key=lambda a: -a.oxygen)

        for astronaut in astronauts:
            astronauts_participate += 1
            for item in planet.items:
                astronaut.backpack.append(item)
                astronaut.breathe()
                if astronaut.oxygen <= 0:
                    continue

        if not planet.items:
            self.successful_missions += 1
            return (f"Planet: {planet_name} was explored. "
                    f"{astronauts_participate} astronauts participated in collecting items.")
        self.not_successful_missions += 1
        return f"Mission is not completed."

    def report(self):
        result = [f"{self.successful_missions} successful missions!",
                  f"{self.not_successful_missions} missions were not completed!",
                  f"Astronauts' info: ",]
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}"
                          f"Oxygen: {astronaut.oxygen}"
                          f"Backpack items: {', '.join(astronaut.backpack) if astronaut.backpack else 'none'}")

        return "\n".join(result)



    # Helping methods:
    @staticmethod
    def _find_element_by_name(name: str, collection):
        element = next(filter(lambda m: m.name == name, collection), None)
        return element

