def print_parity(x):
    if x%2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")

def compare(x, y):
    if x < y:
        print(x, "is less than", y)
    elif x > y:
        print(x, "is greater than", y)
    else:
        print(x, "and", y, "are equal")

def dispatch(choice):
    if choice == "A":
        functionA()
    elif choice == "B":
        functionB()
    elif choice == "C":
        functionC()
    else:
        print("Invalid choice.")
