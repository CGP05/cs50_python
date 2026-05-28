import csv

name = input("what is your name?")
home = input("where is your home?")

with open("names.csv", "a") as file:
          writer = csv.DictWriter(file, fieldnames=["name", "home"])
          writer.writerow({"name": name, "home": home})