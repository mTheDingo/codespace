#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

def main():
    printUserInput()

def printUserInput():
    name = input("First name? :   ").strip().replace(" ", "...")
    print(name)


main()

#This program works as expected thanks to the replace() funtion

#replace() takes in 2 parameters and replaces the given phrases(str)

