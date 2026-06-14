import random


class Tie: 
    parties = ["Liberal", "Conservative", "Bloc Québécois", "New Democratic", "Green"]
        #generally put lists of constants at top of file or class (like this)
    
    def sort(self, name):
        print(name, "is a member of", random.choice(self.parties), "party.")


tie = Tie()
tie.sort("Carney")