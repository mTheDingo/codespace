"""In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
   If the greeting starts with an “h” (but not “hello”), output $20.
 Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
 """


greet = input("Greet : ").lower().strip()

if greet = "hello":
    print("$0")
elif "h" in greet:
   print("$20")
else:
   print("$100")