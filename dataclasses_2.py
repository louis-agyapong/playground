import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.id = generate_id()

    def __str__(self):
        return f"{self.name} ({self.address})"


def main() -> None:
    person = Person("Zion", "13 GT Anguah Ln.")
    print(person)


if __name__ == "__main__":
    main()
