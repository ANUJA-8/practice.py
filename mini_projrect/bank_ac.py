class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Current balance: {self.balance}")

    