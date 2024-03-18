from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    TYPE_ = "IndoorTeam"

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, budget=500)

    def win(self):
        self.advantage += 145
        self.wins += 1
