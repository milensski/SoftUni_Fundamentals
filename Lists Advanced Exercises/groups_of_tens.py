sequence = input().split(", ")
sequence = list(map(int, sequence))

new_list = []
group_counter = 10

while 0<len(sequence):
    for element in sequence:
        if element <= group_counter:
            new_list.append(element)
    print(f"Group of {group_counter}'s: {new_list}")
    group_counter += 10

    for num in new_list:
        if num in sequence:
            sequence.remove(num)
    new_list.clear()

