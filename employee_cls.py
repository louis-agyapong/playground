class Employee:
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"


emp_1 = Employee("Louis", "Agypaong", 50000)
emp_2 = Employee("Nana", "Kyei", 60000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)
