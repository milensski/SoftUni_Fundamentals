sequence = list(map(int, input().split(", ")))

print(sorted(sequence))
group_count = 10
new_list = []
while 0 < len(sequence):
    new_list.clear()
    for element in sequence:
        if int(element) <= group_count:
            sequence.remove(element)
            new_list.append(int(element))
    print(f"Group of {group_count}'s: {new_list}")
    group_count += 10
