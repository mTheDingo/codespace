#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

def main():
    printUserInput()

def printUserInput():
    inp = input("What's your name? :   ")
    print("", inp, sep='...')



main()