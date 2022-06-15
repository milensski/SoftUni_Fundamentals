sequence = input().split()

command = input()

while command != "End":
    index = int(command)
    if index < len(sequence):
        value = int(sequence[index])
        for ind, element in enumerate(sequence):
            element = int(element)
            if element < 0:
                continue
            if element == value and ind == index:
                element = -1
            elif element > value:
                element -= value
            elif element <= value:
                element += value
            sequence.pop(ind)
            sequence.insert(ind, str(element))

    command = input()

shot = sequence.count("-1")

print(f"Shot targets: {shot} -> {' '.join(sequence)}")
