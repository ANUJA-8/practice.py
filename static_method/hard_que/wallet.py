'''Create class Wallet:
owner
balance
daily_limit
Methods:
spend(amount) (only if amount ≤ daily_limit and enough balance)
Create class FinanceControl:
static method increase_limit(wallet, new_limit)
Increase daily limit only if balance > 5000
Print result'''

class Wallet:
	def __init__(self,owner:str,balance:int,daily_limit:int):
		self.owner=owner
		self.balance=balance
		self.daily_limit=daily_limit
	def spend(self,amount):
		if amount<=self.daily_limit and amount<=self.balance:
			self.balance-=amount
			return "Payment Successful"
		else:
			return "No sufficient balance in wallet current balance is {self.balance}"
			
class FinanceControl:
	def increase_limit(li:Wallet,new_limit:int):
		if li.balance>5000:
			li.daily_limit=new_limit
			print(f"New Limit is {li.daily_limit} and current balance is {li.balance}")
		else:
			print("Limit is not increased as there is no sufficient balance")
			
w=Wallet("Anand",6000,4000)
FinanceControl.increase_limit(w,3000)
s=2000
w.spend(s)
print(f"After spending {s}, the balance is {w.balance}")