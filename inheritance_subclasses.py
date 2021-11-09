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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_lang: str) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first: str, last: str, pay: int, employees: list) -> None:
        super().__init__(first, last, pay)
        self.employees = employees

    def add_emp(self, emp: Employee) -> None:
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee) -> None:
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self) -> None:
        for emp in self.employees:
            print(f"--> {emp.fullname()}")


dev_1 = Developer("Teddy", "Agudogo", 10000, "Python")
dev_2 = Developer("Louis", "A", 20000, "Java")

# dev_1.set_raise_amount(1.06)

# print(dev_1.raise_amount)
# print(dev_1.pay)
# print(dev_1.apply_raise())
# print(dev_1.fullname())
# print(dev_1.email)
# print(dev_1.prog_lang)
