'''Create class Employee:
name, salary
method annual_salary()
Create class SalaryCalculator:
static method that returns annual salary'''

class Employee:
	def __init__(self,name:str,salary:int):
		self.name=name
		self.salary=salary
	def annual_salary(self):
		return 12*self.salary	
class SalaryCalculator:
	def annual_sal(sal:Employee):
		# a_salary = sal.annual_salary()
		# print(f"Annual salary of {sal.name} is {a_salary}")
		print(f"{sal.annual_salary()} --- {sal.name}'s annual salary")
		
s=Employee("Anuja", 50000)
SalaryCalculator.annual_sal(s)