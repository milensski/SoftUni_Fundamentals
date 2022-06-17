def swap(lst, index_1, index_2):
    lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
    return lst


def multiply(lst, index_1, index_2):
    lst[index_1] = lst[index_2] * lst[index_1]
    return lst


def decrease(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] - 1
    return lst


sequence = input().split()
sequence = [int(element) for element in sequence]

while True:
    command = input().split()

    if command[0] == "end":
        break
    if command[0] == "swap":
        swap(sequence, int(command[1]), int(command[2]))

    elif command[0] == "multiply":
        multiply(sequence, int(command[1]), int(command[2]))

    elif command[0] == "decrease":
        decrease(sequence)

print(", ".join(map(str, sequence)))
