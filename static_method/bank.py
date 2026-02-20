'''Create a class Account that:
Stores account balance.
Has a method is_minimum() that returns True if balance ≥ 1000.
Create a class Bank that:
Has a static method that prints whether the account maintains minimum balance.'''

class Account:
    def __init__(self, balance):
        self.balance=balance
    def is_minimum(self):
        return self.balance>=1000

class Bank:
    def check_min(account:Account):
        if account.is_minimum():
            print("Account maintains minimum balance.")
        else:
            print("Account does not maintain minimum balance.")

account1=Account(1500)
account2=Account(500)
Bank.check_min(account1)
Bank.check_min(account2)