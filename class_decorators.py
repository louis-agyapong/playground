class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    @property
    def fullname(self) -> str:
        """ "If first or last name is none raise value error"""
        if self.first is None or self.last is None:
            raise ValueError("Name cannot be None")
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name: str) -> None:
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self) -> None:
        print("Delete Name!")
        self.first = None
        self.last = None

    @property
    def email(self) -> str:
        return f"{self.first.lower()}.{self.last.lower()}@company.com"


emp_1 = Employee("Kweku", "Frimpong")
emp_2 = Employee("Kofi", "Asamoah")
emp_1.first = "Kwame"
emp_1.fullname = "Adjoa Adepa"

del emp_2.fullname
emp_2.fullname = "Kofi Asamoah"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print(emp_2.fullname)
