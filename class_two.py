class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year, max_speed):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.fuel_level = 0
        self.fuel_capacity = 100

    def __str__(self) -> str:
        return f"{self.make} {self.model} {self.year}"

    def drive_car(self):
        """Control the cars movement."""
        print("The car is now moving")

    def add_fuel(self, amount):
        """add fuel"""
        fuel_level = self.fuel_level + amount

        if fuel_level > self.fuel_capacity:
            print("Fuel capacity exceeded.")
        elif fuel_level <= self.fuel_capacity:
            print("Fuel added.")


car = Car("Honda", "Civic", "2018", 100)
