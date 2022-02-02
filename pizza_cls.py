class Pizza:
    def __init__(self, ingredients: list) -> None:
        self.ingredients = ingredients

    def __str__(self) -> str:
        return f"Pizza with {', '.join(self.ingredients)}"

    def __repr__(self) -> str:
        return self.ingredients


print(Pizza(["cheese", "tomato"]))
