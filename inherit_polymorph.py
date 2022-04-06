class Dog:
    def __init__(self, name: str, age: int, friendliness: int) -> None:
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self) -> str:
        return "woof!"

    def barks(self) -> str:
        return "Awooooo!"


# class Samoyed(Dog):
#     def __init__(self, name: str, age: int, friendliness: int,
#                  fur_color: str) -> None:
#         super().__init__(name, age, friendliness)
#         self.fur_color = fur_color

#     def likes_walks(self) -> bool:
#         return False


class Samoyed(Dog):
    def __init__(self, name: str, age: int, friendliness: int) -> None:
        super().__init__(name, age, friendliness)

    def barks(self) -> str:
        return "Arf arf!"


class Poodle(Dog):
    def __init__(self, name: str, age: int, friendliness: int) -> None:
        super().__init__(name, age, friendliness)

    def shedding_amount(self) -> int:
        return 0


class GoldenRetriver(Dog):
    def __init__(self, name: str, age: int, friendliness: int) -> None:
        super().__init__(name, age, friendliness)

    def fetch_ability(self) -> int:
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7


class GoldenDoodle(Poodle, GoldenRetriver):
    def __init__(self, name: str, age: int, friendliness: int) -> None:
        super().__init__(name, age, friendliness)

    def barks(self) -> str:
        return "Aroooo!"


if __name__ == "__main__":
    sam = Samoyed("Sam", 2, 5)
    generic_doggo = Dog("Gene", 1, 10)
    goldie = GoldenDoodle("Goldie", 1, 10)

    print(f"Barks: {sam.barks()}")
    print(f"Fetch Ability: {goldie.fetch_ability()}")
    print(f"{goldie.__class__.__name__} barks: {goldie.barks()}")
    print(f"Shedding Amount: {goldie.shedding_amount()}")
    print(f"{generic_doggo.__class__.__name__} barks: {generic_doggo.barks()}")
