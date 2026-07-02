class Package:
    def __init__(self, number, sender, recipient, riding):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.riding = riding


def main():
    packages = [
        Package(number=1, sender="DeeDee", recipient="Mark Carney", riding="Nepean"),
        Package(number=2, sender="Mark Carney", recipient="PP", riding="Battle River—Crowfoot"),
    ]
    for package in packages:
        print(f" Package 1{package.number} from {package.sender} to {package.recipient} in the federal riding of {package.riding}.")

main()
