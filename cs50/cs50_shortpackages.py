class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=2.5),
        Package(number=2, sender="Charlie", recipient="David", weight=1.2)
        
    ]