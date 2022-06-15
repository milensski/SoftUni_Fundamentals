gifts = input().split()

command = input()

while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        if command[1] in gifts:
            word = command[1]
            for i in range(len(gifts)):
                if gifts[i] == word:
                    gifts[i] = "None"

    elif "Required" in command:
        if int(command[2]) >= 0 and int(command[2]) < len(gifts):
            replacement = command[1]
            gifts[int(command[2])] = replacement

    elif "JustInCase" in command:
        index = 1
        if gifts[-1] == "None":
            while gifts[-index] == "None":
                index += 1
            gifts.pop(-index)
            gifts[-index] = command[1]
        else:
            gifts.pop(-index)
            gifts.append(command[1])

    command = input()

while "None" in gifts:
    for element in gifts:
        if element == "None":
            gifts.pop(gifts.index(element))

print(*gifts, sep=" ")
