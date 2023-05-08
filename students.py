
names = []

for _ in range(3):
    names.append(input("What's your name ? "))  #.append -() appends values to the list


for name in sorted(names):  #sorted() sorts the list for us.
    print(f"hello, {name}")
