def main():
    n = int(input("What's n? "))
    for o in otter(n):
        print(o)

def otter(n):
    romp = []
    for i in range(n):
        romp.append("🦦" * i)
    return romp

if __name__ == "__main__":
    main()