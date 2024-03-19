from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST = 2
    TYPE_ = "Student"

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 1
