sequence = input().split()

command = input().split()

while command[0] != "End":

    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if index in range(len(sequence)):
            index_value = int(sequence[index])
            index_value -= value
            if index_value <= 0:
                sequence.pop(index)
            else:
                sequence[index] = str(index_value)

    elif action == "Add":
        if index not in range(len(sequence)):
            print("Invalid placement!")
        else:
            sequence.insert(index, str(value))
    elif action == "Strike":
        if index + value not in range(len(sequence)) and (index - value) not in range(len(sequence)):
            print("Strike missed!")
        else:
            before_radius = index - value
            after_radius = index + value
            sequence = sequence[0:before_radius] + sequence[after_radius + 1::]

    command = input().split()

print("|".join(sequence))
