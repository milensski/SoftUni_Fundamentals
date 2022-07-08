def is_in_range(from_ind, to_ind, field):
    if from_ind >= 0 and from_ind < len(field) and field[from_ind] == 1:
        return True


def move_left(index, lenght, field):
    position = index - lenght

    field[index] = 0
    if position < 0:
        return field

    while field[position] == 1:

        position -= lenght

        if position < 0:
            return field

    else:
        field[position] = 1

    return field


def move_right(index, lenght, field):
    position = index + lenght
    field[index] = 0
    if position >= len(field):
        return field
    while field[position] == 1:
        position += lenght
        if position >= len(field):
            return field
    else:
        field[position] = 1

    return field



n = int(input())

ladybugs = list(map(int, input().split()))
num = 0
field = [num for i in range(n)]

for index in ladybugs:
    if index >= 0 and index < len(field):
        field[index] = 1

while True:

    command = input()

    if command == 'end':
        print(" ".join(list(map(str, field))))
        break

    command = command.split()

    from_index = int(command[0])
    direction = command[1]
    to_index = int(command[2])

    if direction == 'right' and to_index < 0:
        direction = 'left'
    elif direction == "left" and to_index < 0:
        direction = 'right'

    if direction == "right" and is_in_range(from_index, abs(to_index), field):

        move_right(from_index, abs(to_index), field)

    elif direction == "left" and is_in_range(from_index, abs(to_index), field):

        move_left(from_index, abs(to_index), field)
