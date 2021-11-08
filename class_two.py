class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make: str, model: str, year: int, max_speed: int) -> None:
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.fuel_level = 0
        self.fuel_capacity = 100

    def __str__(self) -> str:
        return f"{self.make} {self.model} {str(self.year)}"

    def drive_car(self) -> str:
        """Control the cars movement."""
        return "The car is now moving"

    def calculate_fuel(self, distance: int) -> str:
        """Calculate the current fuel based on distance travelled."""
        return f"Current fuel: {str(self.fuel_level)}"

    def add_fuel(self, amount) -> str:
        """add fuel"""
        fuel_level = self.fuel_level + amount

        if fuel_level > self.fuel_capacity:
            return "Fuel capacity exceeded."
        return "Fuel added."


car = Car("Honda", "Civic", 2018, 100)
