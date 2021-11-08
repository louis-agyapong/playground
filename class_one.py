class Car:
    """
    Represents a car
    """

    smell = "good"

    def __init__(self, speed):
        """
        Initialize attributes to describe a car
        """
        self.speed = speed

    def info(self, color, weight):
        """
        Prints out info about the car
        """
        self.color = color
        self.weight = weight
        return f"This car is {self.color} and weighs {self.weight}"


car_one = Car(100)
car_one.info("red", "2000")

# Dynamic attributes
car_one.x = 10

print(car_one.x)
print(car_one.color, car_one.weight)
print(car_one.speed)
print(car_one.info("blue", "3000"))
