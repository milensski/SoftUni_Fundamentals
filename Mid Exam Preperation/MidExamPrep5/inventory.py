sequence = input().split(", ")

while True:
    command = input()
    if "Craft!" in command:
        break
    command, item = command.split(" - ")
    if command == "Collect":
        if item not in sequence:
            sequence.append(item)
        else:
            continue
    elif command == "Drop":
        if item in sequence:
            sequence.remove(item)
        else:
            continue
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in sequence:
            if sequence.index(old_item)+1 >= len(sequence):
                sequence.append(new_item)
            else:
                sequence.insert(sequence.index(old_item)+1, new_item)
        else:
            continue
    elif command == "Renew":
        if item in sequence:
            sequence.remove(item)
            sequence.append(item)

print(*sequence, sep=", ")
