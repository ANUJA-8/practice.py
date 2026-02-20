'''
1. Create class BankAccount
account_holder
balance
Methods:
deposit(amount)
withdraw(amount)
get_balance()
is_minimum_balance() (minimum balance = 1000)
2. Create class BankService
Static methods:
transfer(sender, receiver, amount)
check_account_status(account)
compare_accounts(acc1, acc2) (who has more balance)'''

class BankAccount:
	def __init__(self,account_holder:str,balance:int):
		self.account_holder=account_holder
		self.balance=balance
	def deposit(self,amount:int):
		self.balance+=amount
		return self.balance
	'''def withdraw(self,amount_w:int):
		if self.balance>= amount_w
			return self.balance-=amount_w
		return f"current balance is less than {self.amount_w} we cannot withdrow money, your current balance is {self.balance}"'''
	def withdraw(self,amount):
		if self.balance>=amount:
			self.balance-=amount
			return self.balance
		return f"current balance is less than {amount} we cannot withdrow money, your current balance is {self.balance}"
	def get_balance(self):
		return self.balance
	def is_minimum_balance(self):
		return self.balance>1000
		#if self.balance<=1000:
			#return f"your current balance is {self.balance} please add more"
		#return f"your balance is {self.balance} and minimum "

class BankService:
	def transfer(sender:BankAccount,receiver:BankAccount,amount:BankAccount):
		if sender.balance >= amount:
			sender.withdraw(amount)
			receiver.deposit(amount)
			print(f"Successfully transferred {amount} from {sender.account_holder} to {receiver.account_holder}")
		else:
			print("Transfer failed: insufficient funds")
			
	def check_account_status(account:BankAccount):
		if account.is_minimum_balance() == True:
			return f"{account.get_balance()} is the current balance"
		
	def compare_accounts(acc1:BankAccount,acc2:BankAccount):
		if acc1.balance> acc2.balance:
			return f" Account 1 has more balance that is {acc1.balance}"
		elif acc1.balance== acc2.balance:
			return "Account one and account 2 has same balance"
		return f"Account 2 has more balance that is {acc2.balance}"
	
ac1=BankAccount("Anuja", 5000)
ac2=BankAccount("Akash", 6000)

BankService.check_account_status(ac1)
BankService.check_account_status(ac2)
print(BankService.compare_accounts(ac1,ac2))
# BankService.transfer(ac2,ac1,1000)

	
	
	
		