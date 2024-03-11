from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    rewards = {1: 1500000, 2: 800000, 8: 20000, 10: 10000}
    EXPENSES = 250000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos in self.rewards:
            revenue = self.rewards[race_pos] - self.EXPENSES
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
