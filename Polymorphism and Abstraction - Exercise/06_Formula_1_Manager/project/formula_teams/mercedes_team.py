from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    rewards = {1: 1500000, 3: 500000, 5: 100000, 7: 50000}
    EXPENSES = 200000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        if race_pos in self.rewards:
            revenue = self.rewards[race_pos] - self.EXPENSES
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
