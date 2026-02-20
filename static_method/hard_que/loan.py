'''Loan Eligibility Checker
Create class Customer:
name
salary
existing_loan (True/False)
Method:
is_eligible()
Eligible if salary > 30000 AND no existing loan
Create class LoanDepartment:
static method approve_loan(customer)
If eligible → increase customer salary by 5000 (simulating raise after loan approval)
Print decision'''

class Customer:
	def __init__(self,name:str, salary:int,existing_loan:int):
		self.name=name
		self.salary= salary
		self.existing_loan=existing_loan
		
	def is_eligible(self):
		if self.salary > 30000 and not self.existing_loan:
			return True
		return False
		
class LoanDepartment:
	def approve_loan(customer:Customer):
		if customer.is_eligible()==True:
			customer.salary+=5000
			print("Loan is approved for",customer.name,"New salary:",customer.salary)
			return
		else:
			print(f"Loan is not approved as {customer.name} is not eligible for the loan")
			return
			
c=Customer("Anand", 40000,4000)
# LoanDepartment.approve_loan(c)
# LoanDepartment.approve_loan(Customer("Ravi", 35000,0))
Customer.is_eligible(c)