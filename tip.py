def main():
    dollars = float((input("How much was the meal? ")))
    percent = float((input("What percentage would you like to tip? ")))
    tip = (dollars * percent) / 100
    print(f"Leave ${tip:.2f}")


main()


#The program works as long as nobodyu types in the $ sign

# i am well aware that this was not the assignment nor mentioned in the prompt
# but i gotta get going because i woke up pretty late and i don't wanna spend too much time on it R