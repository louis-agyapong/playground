"""Property Decorators: Getters, Setters and Deletters"""


class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    def __str__(self) -> str:
        return f"{self.first} {self.last}"

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name) -> None:
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self) -> None:
        print("Delete name!")
        self.first = None
        self.last = None

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"


emp_1 = Employee("Louis", "Agyapong")
emp_1.fullname = "Kweku Frimpong"

print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname
print(emp_1.fullname)
