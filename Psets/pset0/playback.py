#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

def main():
    printUserInput()

def printUserInput():
    name = input("First name? :   ").strip().replace(" ", "...")
    print(name)


main()

#This program works but the prompt is not descriptive enough

#I have wrote a similar program to the one in lecture video so it works

#however it seperates 3 different strings with '...' instead of each space in A string