class Account:

    def __init__(self, _id, name, balance):
        self._id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount >= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f
