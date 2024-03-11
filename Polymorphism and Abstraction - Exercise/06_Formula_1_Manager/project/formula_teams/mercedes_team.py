from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def __init__(self, budget):
        self.budget = budget
        self.expenses = 200000
        self.sponsors = {
            1: 1_100_000,
            2: 600_000,
            3: 600_000,
            4: 100_000,
            5: 100_000,
            6: 50_000,
            7: 50_000,
        }


