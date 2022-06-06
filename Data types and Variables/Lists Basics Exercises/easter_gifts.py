gifts = input().split()
modified_gifts = gifts.copy()
command = input()


while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        if command[1] in gifts:
            word = command[1]
            for i in range(len(gifts)):
                if gifts[i] == word:
                    gifts.remove(word)

    elif "Required" in command:
        if int(command[2]) <= len(gifts):
            replacement = command[1]
            gifts[int(command[2])] = replacement

    elif "JustInCase" in command:
        gifts.pop()
        gifts.append(command[1])
    command = input()
print(gifts)

