class Package:
    def __init__(self, number, sender, recipient, riding, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.riding = riding
        self.weight = weight

    def __str__(self):
        return f"This is a package {self.number} from {self.sender} to {self.recipient} in the federal riding of {self.riding} with a weight of {self.weight} kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

def main():
    packages = [
        Package(number=1, sender="DeeDee", recipient="Mark Carney", riding="Nepean", weight=1.5),
        Package(number=2, sender="Mark Carney", recipient="PP", riding="Battle River—Crowfoot", weight=2.5),
    ]
    for package in packages:
        print(f" and {package} costs {package.calculate_cost(cost_per_kg=12)} CAD")

main()