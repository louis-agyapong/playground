class Employee:
    num_of_employees = 0
    raise_amount: float = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_employees += 1

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


print(Employee.num_of_employees)
emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Kweku", "Frimpong", 5000)
print(Employee.num_of_employees)
emp_3 = Employee("Justine", "Naylor", 80000)
emp_4 = Employee("Ama", "Mansa", 40000)

print(Employee.num_of_employees)