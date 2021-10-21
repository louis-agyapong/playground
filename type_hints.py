from typing import List, Dict


def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_length(full_name: str) -> int:
    return len(full_name)


def get_name_with_age(full_name: str, age: int) -> str:
    return f"{full_name} is {age}"


def get_names_with_ages(names: List[str], ages: List[int]) -> List[str]:
    return [f"{name} is {age}" for name, age in zip(names, ages)]


def process_items(items: List[int]) -> List[int]:
    return [item * 2 for item in items]


def process_food_prices(prices: Dict[str, float]):
    for item, price in prices.items():
        print(f"{item} costs ${price}")
    return prices


print(get_full_name(last_name="jane", first_name="doe"))
print(get_name_length("jane doe"))
print(get_name_with_age("jane doe", 30))
print(get_names_with_ages(["jane", "john"], [30, 40]))
print(process_items([1, 2, 3]))
print(process_food_prices({"apple": 1.0, "banana": 2.0}))
