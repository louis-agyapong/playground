numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def doubled_odds(numbers: list) -> list:
    """
    Given a list of numbers, return a list where
    all odd numbers are doubled (HINT: use forloop)
    """
    doubled_odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            doubled_odd_numbers.append(number * 2)
    return doubled_odd_numbers


def doubled_odds_v2(numbers: list) -> list:
    """
    Given a list of numbers, return a list where
    all odd numbers are doubled (HINT: use filter, odd?)
    """
    return list(filter(lambda x: x % 2 != 0, map(lambda x: x * 2, numbers)))


print(doubled_odds_v2(numbers))
