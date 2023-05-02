#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

def main():
    printUserInput()

def printUserInput():
    inp = input("What would you like to say ? :   ")
    print("", f"{inp}", sep='...')



main()