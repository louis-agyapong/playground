class Employee:

    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self) -> str:
        return f"{self.first.title()} {self.last.title()}"

    def apply_raise(self) -> None:
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee("louis", "agyapong", 50000)
emp_2 = Employee("nana", "kyei", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
