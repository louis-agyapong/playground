import datetime


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


emp_1 = Employee("Kweku", "Frimpong", 50000)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)

emp_str_1 = "John-Doe-70000"
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email, new_emp_1.pay)


my_date = datetime.date(2020, 7, 21)
print(Employee.is_work_day(my_date))
