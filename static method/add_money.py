'''Create class Wallet:
balance
method add_money(amount)
Create class Transaction:
static method that deposits money into wallet'''

class Wallet:
	def __init__(self,balance:int):
		self.balance=balance
	def add_money(self,amount):
		self.balance+=amount
		
class Transaction:
	def deposits(total:Wallet,amount):
		print(f"{total.add_money(amount)} is added to the wallet. Current balance is {total.balance}")
		
bal=Wallet(40000)
Transaction.deposits(bal, 5000)