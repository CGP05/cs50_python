class Package:
    def __init__(self, number, sender, recipient, riding):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.riding = riding

def main():
    packages = [
        Package(number=1, sender="DeeDee", recipient="Mark Carney", riding=Nepean),
        Package(number=2, sender="Mark Carney", recipient="PP", riding=Bow River)
        
    ]