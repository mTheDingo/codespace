"""
implement a program in Python that prompts the user for input and then outputs that same input in lowercase.

"""

def main():
    printUserInput()


def printUserInput():
   inp = input("What would you like to say?").lower()
   print(inp)


main()