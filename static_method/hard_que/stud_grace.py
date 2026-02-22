'''Create class Student:
name
marks
Methods:
add_grace_marks(amount)
is_pass() (pass if ≥ 40)
Create class ExamBoard:
static method re_evaluate(student)
If student failed, add 5 grace marks
Print final result'''

class Student:
	def __init__(self,name:str,marks:int):
		self.name=name
		self.marks=marks
	def add_grace_marks(self,amount):
		self.marks+=amount
		return self.marks
	def is_pass(self):
		return self.marks>=40
		
class ExamBoard:
	def re_evaluate(stud:Student):
		if not stud.is_pass():
			print(f"As {stud.name} is failed so by adding grace marks it will be {stud.add_grace_marks(5)}")
		if stud.is_pass():      #double if statement helps to throw result if the grace marks are added but still the student is failed to paass next result we use double if statement here
			print(f"As the student is pass no grace marks needed marks are {stud.marks}")
		else:
			print(f"Still failed by adding grace marks and updated marks are {stud.marks}")
			
st=Student("Ana", 25)
ExamBoard.re_evaluate(st)