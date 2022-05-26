
command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for i in range(len(command)):
        print(f"{command[i]*2}", end= "")

    command = input("\n")