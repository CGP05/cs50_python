class Package:
    def __init__(self, number, sender, recipient, riding):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.riding = riding

    def __str__(self):
        return f"This is a package {self.number} from {self.sender} to {self.recipient} in the federal riding of {self.riding}."


def main():
    packages = [
        Package(number=1, sender="DeeDee", recipient="Mark Carney", riding="Nepean"),
        Package(number=2, sender="Mark Carney", recipient="PP", riding="Battle River—Crowfoot"),
    ]
    for package in packages:
        print(package)

main()