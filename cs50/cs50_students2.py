class Politician:
    def __init__(self, name, party):
        if not name:
            raise ValueError("Missing name")
        if party not in ["Liberal", "Conservative", "Bloc Quebecois", "New Democratic"]:
            raise ValueError("Invalid party")
        self.name = name
        self.party = party


    def __str__(self):
        return f"MP {self.name} from {self.party} party"
    
    def ideology(self):
        match self.party:
            case "Liberal":
                return "centrist liberalism"
            case "Conservative":
                return "right-wing populism"
            case "Bloc Quebecois":
                return "Quebec separatism"
            case "New Democratic":
                return "democratic socialism"

def main():
    politician = get_politician()
    politician.party = "24 Sussex Drive"
    print(politician)


def get_politician():
    name = input("Name: ")
    party = input("Party: ")
    return Politician(name, party)

if __name__ == "__main__":
    main()