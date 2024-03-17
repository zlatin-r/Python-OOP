from typing import List

from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS_TYPES:
            return f"{diver_type} is not allowed in our competition."
        if self.find_diver(diver_name):
            return f"{diver_name} is already a participant."
        new_diver = self.VALID_DIVERS_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."
        if self.find_fish(fish_name):
            return f"{fish_name} is allowed for chasing as a {fish_type}."
        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.find_diver(diver_name)
        fish = self.find_fish(fish_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                count += 1
                diver.update_health_status()
                diver.renew_oxy()
            return f"Divers recovered: {count}"

    def competition_statistics(self):
        divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result = "**Nautical Catch Challenge Statistics**"
        result += "\n".join(sorted_divers)


    def find_diver(self, diver_name: str):
        return next(filter(lambda d: d.name == diver_name, self.divers), None)

    def find_fish(self, fish_name: str):
        return next(filter(lambda f: f.name == fish_name, self.fish_list), None)
