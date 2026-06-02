class Politician:
    def __init__(self, name, party):
        if not name:
            raise ValueError("Missing name")
        if party not in ["Liberal", "Conservative", "Bloc", "New Democratic"]:
            raise ValueError("Invalid party")
        self.name = name
        self.party = party
        
    def __str__(self):
        return f"MP {self.name} from {self.party} party"
    
    def ideology(self):
        match self.party:
            case "Liberal":
                return " centrist liberalism"
            case "Conservative":
                return "right-wing populism"
            case "Bloc":
                return "Quebec seperatism"
            case "NDP":
                return "democratic socialism"

def main():
    politician = get_politician()
    print(politician)

def get_politician():
    name = input("Name: ")
    party = input("Party: ")
    return Politician(name, party)

if __name__ == "__main__":
    main()