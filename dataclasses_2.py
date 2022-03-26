import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass(kw_only=True, slots=True)
class Person:
    name: str
    address: str
    id: str = field(init=False, default_factory=generate_id)
    email_addresses: list = field(default_factory=list)
    active: bool = True
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="Zion", address="13 GT Anguah Ln.")
    print(person)


if __name__ == "__main__":
    main()
