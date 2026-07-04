class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("hi I am a cute cat. meow!")


cat = Cat()
cat.meow()