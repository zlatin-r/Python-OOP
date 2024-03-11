from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    rewards = {1: 1500000, 3: 500000, 5: 100000, 7: 50000}
    EXPENSES = 200000
    REV = 0

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos in self.rewards:
            self.REV = self.rewards[race_pos] - self.EXPENSES
            self.budget += self.REV
            return f"The revenue after the race is {self.REV}$. Current budget {self.budget}$"
