'''Student & ResultCalculator
Create Student class with: name, marks
with methods:
check_pass(student)
calculate_grade(student)
Create ResultCalculator to call these methods and print the result'''

class Student:
    def __init__(self,name:str,marks:int):
        self.name=name
        self.marks=marks
    def check_pass(self):
        if self.marks>=40:
            return f"{self.name} is passed"
        return f"{self.name} is failed"
    def calculate_grade(self):
        if self.marks>=90:
            return f"{self.name} got A grade"
        elif self.marks>=80:
            return f"{self.name} got B grade"   
        elif self.marks>=70:
            return f"{self.name} got C grade"
        elif self.marks>=60:
            return f"{self.name} got D grade"
        elif self.marks>=40:
            return f"{self.name} got E grade"
        else:
            return f"{self.name} got F grade"

class ResultCalculator:
    def result(self,student:Student):
        print(student.check_pass())
        print(student.calculate_grade())

s1=Student("Akash", 85)
s2=Student("Meghna", 35)
result_calculator=ResultCalculator()
result_calculator.result(s1)
# result_calculator.result(s2)
ResultCalculator.calculate_grade(s1)
ResultCalculator.check_pass(s2)

    

