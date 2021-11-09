class Employee:
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"

    def fullname(self) -> str:
        return f"{self.first} {self.last}"


emp_1 = Employee("Kweku", "Frimpong", 50000)
emp_2 = Employee("Nana", "Yeboah", 60000)

print(emp_1)
print(emp_2)
print(emp_1.fullname())
