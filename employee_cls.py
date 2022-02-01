class Employee:
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self) -> str:
        return f"{self.first.title()} {self.last.title()}"


emp_1 = Employee("louis", "agyapong", 50000)
emp_2 = Employee("nana", "kyei", 60000)

print(emp_1)
print(emp_2)

print(emp_1.fullname())
print(emp_2.fullname())
