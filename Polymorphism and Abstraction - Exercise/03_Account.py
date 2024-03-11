class Account:

    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if transaction_amount > self.amount:
            raise ValueError("sorry cannot go in debt!")

        self.amount -= transaction_amount
        self._transactions.append(transaction_amount)

        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not amount.isdigit():
            raise ValueError("please use int for amount")
        if self.amount < amount:
            raise ValueError("sorry cannot go in debt!")

        self.amount -= amount
        self._transactions.append(amount)

        return f"New balance: {self.amount}"

    def balance(self):
        return sum(self._transactions) + self.amount

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __lt__(self, obj):
        return self.balance < obj.balance

    def __le__(self, obj):
        return self.balance <= obj.balance

    def __eq__(self, obj):
        return self.balance == obj.balance

    def __ne__(self, obj):
        return self.balance != obj.balance

    def __gt__(self, obj):
        return self.balance > obj.balance

    def __ge__(self, obj):
        return self.balance >= obj.balance

    def __add__(self, obj):
        concatenate_two_accounts = Account(f"{self.owner}&{obj.owner}", self.amount + obj.amount)
        concatenate_two_accounts._transactions = self._transactions + obj._transactions
        return concatenate_two_accounts

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"


