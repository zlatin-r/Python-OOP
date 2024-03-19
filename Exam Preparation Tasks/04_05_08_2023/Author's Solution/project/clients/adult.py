from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INTEREST = 4.0
    INTEREST_INCREMENT = 2.0
    POSSIBLE_LOAN_TYPE = 'MortgageLoan'

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INTEREST)

    def increase_clients_interest(self):
        self.interest += self.INTEREST_INCREMENT
