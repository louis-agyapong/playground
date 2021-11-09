class Employee:
    num_of_employees = 0
    raise_amount: float = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@company.com"

        Employee.num_of_employees += 1

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"

    def __repr__(self) -> str:
        return f"{self.first} {self.last} {self.pay}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self) -> int:
        return len(self.fullname())

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise_amount(cls, amount) -> None:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Kweku", "Frimpong", 5000)
emp_2 = Employee("Nana", "Yaw", 200000)
# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__str__())
# print(emp_1.__repr__())
# print(1 + 2)
# print(int.__add__(1, 2))
# print(int.__sub__(3, 1))
# print(str.__add__("Kofi", ' Asamoah'))

print(emp_1 + emp_2)
print(emp_1.__add__(emp_2))
print(len(emp_1))
