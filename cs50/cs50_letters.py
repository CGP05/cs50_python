def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Obama", "Marmot Dumpling"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
    return f'''

    Dear {receiver},

    You are invited to a ball at Peach's Castle tonight!"

    Love,
    {sender}

    '''


main()
