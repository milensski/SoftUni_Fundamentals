command = input()
coffee = 0

while command != "END":
    if command.islower():
        if command == "coding" or command == "dog" or command == "cat" or command == "movie":
            coffee += 1
    else:
        coffee += 2
    if coffee > 5:
        print("You need extra sleep")
        exit()
    command = input()
print(coffee)