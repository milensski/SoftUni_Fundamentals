def operation(sequence, removed_element):
    temporary_list = []
    for element in sequence:
        if element > removed_element:
            element -= removed_element
            temporary_list.append(element)
        elif element <= removed_element:
            element += removed_element
            temporary_list.append(element)
    return temporary_list


sequence = input().split()
sequence = list(map(int, sequence))

popped_elements = []
last_element = 0

while len(sequence) != 0:
    index = int(input())

    removed_element = 0

    if index >= 0 and index < len(sequence):
        removed_element = sequence.pop(index)
        popped_elements.append(removed_element)
        sequence = operation(sequence, removed_element)
    elif index < 0:
        removed_element = sequence.pop(0)
        popped_elements.append(removed_element)
        last_element = sequence[-1]
        sequence.insert(0, last_element)

        sequence = operation(sequence, removed_element)
    elif index >= len(sequence):
        removed_element = sequence.pop()
        popped_elements.append(removed_element)
        first_element = sequence[0]
        sequence.append(first_element)
        sequence = operation(sequence, removed_element)

print(sum(popped_elements))
