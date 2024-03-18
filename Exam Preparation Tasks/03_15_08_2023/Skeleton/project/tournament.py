from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            return ValueError("Invalid equipment type!")
        new_equipment = self.VALID_EQUIPMENT[equipment_type]
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise ValueError("Invalid team type!")
        if self.capacity <= 0:
            return "Not enough tournament capacity."
        new_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self._find_equipment(equipment_type)
        team = self._find_team(team_name)

        if team.budget < equipment.PRICE:
            raise Exception("Budget is not enough!")
        team.budget -= equipment.PRICE
        team.equipment.append(equipment)
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._find_team(team_name)
        if not team:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."  # TODO Check if alwayse return

    def increase_equipment_price(self, equipment_type: str):
        changed_eq_pcs = len([eq.increase_price() for eq in self.equipment if eq.TYPE_ == equipment_type])
        return f"Successfully changed {changed_eq_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._find_team(team_name1)
        team2 = self._find_team(team_name2)

        if type(team1).__name__ != type(team2).__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + sum(e.protection for e in team1.equipment)
        team2_points = team2.advantage + sum(e.protection for e in team2.equipment)

        if team1_points == team2_points:
            return "No winner in this game."

        if team1_points > team2_points:
            team1.win()
        else:
            team2.win()

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [(f"Tournament: {self.name}\n"
                   f"Number of Teams: {len(self.teams)}\n"
                   "Teams:\n")]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

    def _find_equipment(self, equipment_type: str):
        collection = [eq for eq in self.equipment if eq.TYPE_ == equipment_type]
        return collection[-1] if collection else None

    def _find_team(self, team_name: str):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None
