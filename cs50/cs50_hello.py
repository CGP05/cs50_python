#ask user for their name and remove white space and capitalize
name = input("What is your name? ").strip().title()

#split name into first and last
first, last = name.split(" ")

#say hello to user
print(f"hello, {name}")
