sequence = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command.split()
    if command[0] == "Urgent":
        if command[1] in sequence:
            sequence.insert(0, command[1])
        else:
            continue
    if command[0] == "Unnecessary":
        if command[1] in sequence:
            sequence.remove(command[1])
        else:
            continue
    if command[0] == "Correct":
        if command[1] in sequence:
            sequence[sequence.index(command[1])] = command[2]
    else:
        continue
    if command[0] == "Rearrange":
        if command[1] in sequence:
            sequence.remove(command[1])
            sequence.append(command[1])
        else:
            continue

print(*sequence, sep=", ")
