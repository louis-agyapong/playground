import datetime


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

    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day: str) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("louis", "agyapong", 50000)
emp_2 = Employee("nana", "kyei", 60000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"
emp_str_4 = "Kenny-Smith-17000"


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


my_date = datetime.date(2020, 7, 21)
print(Employee.is_workday(my_date))
