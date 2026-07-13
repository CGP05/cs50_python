def main():
    n = int(input("What's n? "))
    for o in otter(n):
        print(o)


def otter(n): #helper function
    for i in range(n):
        yield "🦦" * i

if __name__ == "__main__":
    main()