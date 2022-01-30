class Dog:
    # class object attribute
    species = "Canis familiaris"

    def __init__(self, name: str, age: int) -> None:
        # instance attributes
        self.name = name
        self.age = age

    # instance method
    def description(self) -> str:
        return f"{self.name} is {self.age} years old"

    # instance method
    def speak(self, sound: str) -> str:
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 6)
miles = Dog("Miles", 4)

print(buddy.description())
print(buddy.speak("Woof!"))
