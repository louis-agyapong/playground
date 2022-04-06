from black import main


class Dog:
    def __init__(self, name: str, age: int, friendliness: bool) -> None:
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self) -> bool:
        return True


# class Samoyed(Dog):
#     def __init__(self, name: str, age: int, friendliness: bool,
#                  fur_color: str) -> None:
#         super().__init__(name, age, friendliness)
#         self.fur_color = fur_color

#     def likes_walks(self) -> bool:
#         return False


class Samoyed(Dog):
    def __init__(self, name: str, age: int, friendliness: bool) -> None:
        super().__init__(name, age, friendliness)


if __name__ == "__main__":
    sam = Samoyed("Sam", 2, True)
    print(sam.name, sam.age, sam.friendliness, sam.likes_walks())
