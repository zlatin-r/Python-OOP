from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    _VALID_WAITER_TYPES = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    _VALID_CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self._VALID_WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."

        try:
            next(filter(lambda w: w.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."
        except StopIteration:
            self.waiters.append(self._VALID_WAITER_TYPES[waiter_type](waiter_name, hours_worked))
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self._VALID_CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."

        try:
            next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} is already a client."
        except StopIteration:
            self.clients.append(self._VALID_CLIENT_TYPES[client_type](client_name))
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self,waiter_name: str):


