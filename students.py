name = input("What's your name? ")
last = input("What's your last name? ")

with open("names.txt", "a") as file:
     file.write(f"{name}, {last}\n")