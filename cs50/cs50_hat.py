import random


class Tie: 
    parties = ["Liberal", "Conservative", "Bloc Québécois", "New Democratic", "Green"]
        #generally put lists of constants at top of file or class (like this)
    
    @classmethod
    def sort(cls, name):
        print(name, "is a member of", random.choice(cls.parties), "party.")


Tie.sort("Carney")