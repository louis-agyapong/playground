
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

if __name__ == "__main__":
    item1 = InventoryItem("Widget", 10, 5)
    print(item1.name)
    print(item1.total_cost())

