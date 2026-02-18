class Employee:
    def __init__(self, id: int, name: str, salary: float, dep: str):
        self.id = id
        self.name = name
        self.salary = salary
        self.dep = dep

    def __eq__(self, other: "Employee"):
        return self.name == other.name
        # return self.salary == other.salary

    def __str__(self):
        return f"{self.id} {self.name} {self.salary} {self.dep}"	


class Department:
    def __init__(self, name_department: str):
        self.dpname = name_department
        self.employees = []   # Correct way to initialize list

    def add_emp(self, emp: "Employee"):
        if emp.dep!=self.dpname :
            return f"{emp.name} is not from that department"
        if emp not in self.employees:
            self.employees.append(emp)
            return f"{emp.name} added to department {self.dpname}"
        return f"{emp.name} is already added in department {self.dpname}"

e1 = Employee(1, "Akash", 50000, "IT")
e2 = Employee(2, "Meghna", 60000, "HR")
e3 = Employee(1, "Akash", 70000, "IT")
de=Department("IT")
print(de.add_emp(e1))
print(de.add_emp(e1))
print(de.add_emp(e2))
print(e1)
print(e1 == e3)
print(e1.__eq__(e3))
