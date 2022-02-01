class Employee:

    num_of_emplyees = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emplyees += 1

    def fullname(self) -> str:
        return f"{self.first.title()} {self.last.title()}"

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("louis", "agyapong", 50000)
emp_2 = Employee("nana", "kyei", 60000)

# print(emp_1.__dict__)
print(Employee.num_of_emplyees)
