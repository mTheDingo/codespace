"""In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
 outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No."""




answer = input("Enter your answer to the Great Question of Life :  ").lower().strip().split()

match answer:
    case "42" | "fourty two" | "fourty-two":
        print("YES")
    case _:
        print("NO")


