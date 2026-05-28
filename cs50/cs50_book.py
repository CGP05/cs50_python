def main():
    with open(r"C:\Users\chris\Documents\2025 canadian federal election results.txt", "r") as f:
        contents = f.readlines()

    etobicoke_centre = contents[1729:1734]
    with open("etobicoke_centre.txt", "w") as f:
        f.writelines(etobicoke_centre)

main()