from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_BREED_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.VALID_HORSE_BREED_TYPES:

            try:
                next(filter(lambda h: h.name == horse_name, self.horses))
                raise Exception(f"Horse {horse_name} has been already added!")
            except StopIteration:
                self.horses.append(self.VALID_HORSE_BREED_TYPES[horse_type](horse_name, horse_speed))
                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        try:
            next(filter(lambda j: j.name == jockey_name, self.jockeys))
            raise Exception(f"Jockey {jockey_name} has been already added!")
        except StopIteration:
            self.jockeys.append(Jockey(jockey_name, age))
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        try:
            next(filter(lambda r: r.race_type == race_type, self.horse_races))
            raise Exception(f"Race {race_type} has been already created!")
        except StopIteration:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._find_jockey_by_name(jockey_name)
        horse = self._find_horse_by_type(horse_type)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse"

        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self._find_race_by_type(race_type)
        jockey = self._find_jockey_by_name(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if next(filter(lambda j: j.name == jockey_name, race.jockeys), None):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def _find_race_by_type(self, race_type: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        return race

    def _find_horse_by_type(self, horse_type: str):
        for i in range(len(self.horses) - 1, -1, -1):
            if self.horses[i].TYPE_ == horse_type:
                if not self.horses[i].is_taken:
                    return self.horses.pop(i)
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def _find_jockey_by_name(self, jockey_name: str):
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        return jockey
