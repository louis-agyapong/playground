class Pizza:
    def __init__(self, ingredients: list, radius: float = 2.0) -> None:
        self.ingredients = ingredients

    def __str__(self) -> str:
        return f"Pizza with {', '.join(self.ingredients)}"

    def __repr__(self) -> str:
        return self.ingredients

    @classmethod
    def margharita(cls):
        return cls(["cheese", "tomaotes"])

    @classmethod
    def prosciutto(cls):
        return cls(["cheese", "tomatoes", "ham", "mushrooms"])

    @staticmethod
    def is_vegetarian(pizza: "Pizza") -> bool:
        return "cheese" in pizza.ingredients


marg = Pizza.margharita()
pros = Pizza.prosciutto()

print(marg)
print(pros)
print(marg.is_vegetarian(marg))
