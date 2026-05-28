name = input("what is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print ("Gryffindor")
    case "Herminone":
        print("Gryffindor")
    case "Ron":
        print("Gryffinfor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
