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

    def process_shifts(self, waiter_name: str):
        try:
            waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            points_earned = int(client.earning_points(order_amount))
            return f"{client_name} earned {points_earned} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            discount, remaining_points = client.apply_discount()
            return f"{client_name} received a {discount}% discount. Remaining points {int(remaining_points)}"
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: -w.calculate_earnings())

        total_earnings = sum([w.calculate_earnings() for w in self.waiters])
        total_unused_client_points = sum([c.points for c in self.clients])
        total_clients = len(self.clients)

        result = [f"$$ Monthly Report $$\n"
                  f"Total Earnings: ${total_earnings:.2f}\n"
                  f"Total Clients Unused Points: {int(total_unused_client_points)}\n"
                  f"Total Clients Count: {total_clients}\n"
                  f"** Waiter Details **"]

        for waiter in sorted_waiters:
            result.append(waiter.__str__())

        return "\n".join(result)
