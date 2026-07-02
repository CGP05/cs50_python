class Food:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    
    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = 1
        for ingredient in ingredients:
            hearts += 1
        return hearts


def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    ...

main()