class Student:
    def __init__(self, name, party):
        if not name:
            raise ValueError("Missing name")
        if party not in ["Liberal", "Conservative", "Bloc", "NDP"]:
            raise ValueError("Invalid party")
        self.name = name
        self.party = party

    def __str__(self):
        return f"{self.name} from {self.party}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    party = input("Party: ")
    return Student(name, party)

if __name__ == "__main__":
    main()