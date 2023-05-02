"""In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""


# prompt the user for a mass as an integer
m = int(input("Mass: "))
# output the equivalent number of joules as an integer
c =300000000
E = pow(m + c, 2)

print(E)
