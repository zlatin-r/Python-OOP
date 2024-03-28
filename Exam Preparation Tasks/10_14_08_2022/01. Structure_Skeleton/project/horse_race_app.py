from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import ThoroughBred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_BREED_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": ThoroughBred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.VALID_HORSE_BREED_TYPES.keys():
            if self._find_horse_by_name(horse_name):
                raise ValueError(f"Horse {horse_name} has been already added!")

            new_horse = self.VALID_HORSE_BREED_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self._find_jockey_by_name(jockey_name):
            raise ValueError(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self._check_if_race_type_already_created(race_type):
            raise ValueError(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horses.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        filtered_horses = [h for h in self.horses if type(h).__name__ == horse_type and not h.is_taken]
        if not filtered_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            raise Exception(f"Jockey {jockey_name} already has a horse.")

        horse = filtered_horses.pop()
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not self._check_if_race_type_is_valid(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self._find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if self._check_if_jokey_is_added_in_the_race(jockey_name, race_type):
            raise Exception(f"Jockey {jockey_name} has been already added to the {race_type} race.")

        self.horse_races.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        best_speed = 0
        winner = ""
        for jockey in race:
            if jockey.horse.speed > best_speed:
                winner = Jockey(jockey.horse.name, jockey.horse)

        return (f"The winner of the {race_type} race, "
                f"with a speed of {winner.horse.speed}km/h is "
                f"{winner.name}! Winner's horse: {winner.horse.name}.")

    # HELPING METHODS

    def _find_horse_by_name(self, horse_name: str):
        horse = next(filter(lambda h: h.name == horse_name, self.horses), None)
        return horse

    def _find_jockey_by_name(self, jockey_name: str):
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)
        return jockey

    def _check_if_race_type_already_created(self, race_type: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        return race

    def _check_if_race_type_is_valid(self, race_type: str):
        return race_type in ["Winter", "Spring", "Autumn", "Summer"]

    def _check_if_jokey_is_added_in_the_race(self, joke_name: str, race_type: str):
        races = [r for r in self.horse_races if r.race_type == race_type]
        if races:
            return next(filter(lambda j: j.joke_name == joke_name, races), None)

    def _find_race_by_type(self, race_type: str):
        return next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
