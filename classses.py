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

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


buddy = Dog("Buddy", 6)
miles = Dog("Miles", 4)

print(buddy.description())
print(buddy.speak("Woof!"))
print(miles)


class Car:
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f"The {self.color} car has {self.mileage:,} miles."


blue_car = Car("blue", 20_000)
red_car = Car("red", 30_000)

print(blue_car)
print(red_car)
