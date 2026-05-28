def main():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n = int(input("what is n?" ))
        if n >0:
            break
        return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
