'''Create class Student:
name, marks
method get_marks()
Create class TopperFinder:
static method that compares two students
prints topper name'''
class Student:
	def __init__(self,name:str, marks:int):
		self.name=name
		self.marks=marks
	def get_marks(self):
		return self.marks	
class Topper:
	def Topper_name(m1:Student,m2:Student):
		if m1.get_marks()>m2.get_marks():
			print(f"{m1.name} is topper")
		elif m1.get_marks()== m2.get_marks():
			print(f" Both have equal marks")
		else:
			print(f"{m2.name} is topper")
		
st1=Student("Anuja", 60)
st2=Student("Akash", 50)
Topper.Topper_name(st1,st2)