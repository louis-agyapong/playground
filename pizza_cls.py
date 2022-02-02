class Pizza:
    def __init__(self, ingredients: list) -> None:
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


marg = Pizza.margharita()
pros = Pizza.prosciutto()

print(marg)
print(pros)
