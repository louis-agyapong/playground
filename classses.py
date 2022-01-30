class Dog:
    # class object attribute
    species = "Canis familiaris"

    def __init__(self, name: str, age: int) -> None:
        # instance attributes
        self.name = name
        self.age = age


buddy = Dog("Buddy", 6)
miles = Dog("Miles", 4)

print(buddy.name)
print(miles.name)
