sequence = input().split()
#    0   1  2
command = input().split()

while command[0] != "End":

    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if 0 <= index < len(sequence):
            index_value = int(sequence[index])
            index_value -= value
            if index_value <= 0:
                sequence.pop(index)
            else:
                sequence[index] = f'{index_value}'

    elif action == "Add":
        if 0 > index or index >= len(sequence):
            print("Invalid placement!")
        else:
            sequence.insert(index, str(value))
    elif action == "Strike":
        if (index - value) < 0 or (index + value) >= len(sequence):
            print("Strike missed!")
        else:
            before_radius = index - value
            after_radius = index + value
            sequence = sequence[0:before_radius] + sequence[after_radius + 1::]

    command = input().split()

print("|".join(sequence))
