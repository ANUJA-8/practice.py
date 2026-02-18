class Student:
    def __init__(self, marks_list):
        self.marks_list = marks_list 
    def count_passed(self):
        count = 0
        for marks in self.marks_list:
            if marks > 50:
                count += 1
        return count

class Passed:
    @staticmethod
    def total_passed(student_obj: Student):
        total = student_obj.count_passed()
        print(f"Total students passed (marks > 50): {total}")


marks = [35, 60, 75, 20, 90, 50, 55]
student = Student(marks)
Passed.total_passed(student)
