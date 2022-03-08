from dataclasses import dataclass


class InventoryItem:
    """
    Class for keeping track of an item in inventory.
    will be refactored to use dataclasses.
    """

    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0) -> None:
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


@dataclass
class Student:
    name: str
    major: str
    gpa: float

    def on_honor_roll(self) -> bool:
        if self.gpa >= 3.5:
            return True
        else:
            return False


"""
Create a small application that asks the users to type in
a word and check the users word against a list of existing
words.
"""


if __name__ == "__main__":
    item1 = InventoryItem("Widget", 10, 5)
    student = Student("John", "Math", 3.5)
    print(item1.name)
    print(item1.total_cost())
