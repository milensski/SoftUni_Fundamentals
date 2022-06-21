def is_in_range(from_ind, to_ind, field):
    if from_ind >= 0 and from_ind < len(field):
        if from_ind + to_ind < len(field) or from_ind - to_ind >= 0:
            return True
        else:
            return False


def move_left(index, lenght, field):
    position = index - lenght
    position = abs(position)
    field[index] = 0
    if position < 0:
        return field
    while field[position] == 1:
        position -= 1
        if position < 0:
            break
    else:
        field[position] = 1

    return field


def move_right(index, lenght, field):
    position = index + lenght
    field[index] = 0
    if position >= len(field):
        return field
    while field[position] == 1:
        position += 1
        if position >= len(field):
            break
    else:
        field[position] = 1

    return field


n = int(input())

ladybugs = list(map(int, input().split()))
num = 0
field = [num for i in range(n)]

for index in ladybugs:
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

    if direction == "right" and is_in_range(from_index, to_index, field):

        move_right(from_index, abs(to_index), field)

    elif direction == "left" and is_in_range(from_index, to_index, field):

        move_left(from_index, abs(to_index), field)

