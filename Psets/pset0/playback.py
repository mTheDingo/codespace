#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

def main():
    printUserInput()

def printUserInput():
    first = input("First name? :   ")
    last = input("Last name? :  ")
    print("Hello", first, last, sep='...')



main()