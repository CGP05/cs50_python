import random

class Tie: 
    def __init__(self):
        self.parties = ["Liberal", "Conservative", "Bloc", "New Democratic", "Green"]
        #generally put lists of constants at top of file or class (like this)
    
    def sort(self, name):
        print(name, "is in", random.choice(self.parties))


tie = Tie()
tie.sort("Carney")