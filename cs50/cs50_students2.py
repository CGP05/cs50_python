class Politician:
    def __init__(self, name, party):
        self.name = name
        self.party = party

    def __str__(self):
        return f"MP {self.name} from {self.party} party"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        party = input("Party: ")
        return cls(name, party)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def party(self):
        return self._party
    
    @party.setter
    def party(self, party):
        if party not in ["Liberal", "Conservative", "Bloc Quebecois", "New Democratic", "Green"]:
            raise ValueError("Invalid party")
        self._party = party
    #this function protects the data on the way in and from being overriden

def main():
    politician = Politician.get()
    print(politician)
    
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


if __name__ == "__main__":
    main()