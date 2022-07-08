def add(lesson_title, lst):
    if lesson_title not in lst:
        lst.append(lesson_title)

    return lst


def insert(lesson_title, index, lst):
    if index >= 0 and index < len(lst):
        if lesson_title not in lst:
            sequence.insert(index, lesson_title)
    return lst


def remove(lesson_title, lst):
    lesson_exercise = f'{lesson_title}-Exercise'
    if lesson_title in lst:
        lst.remove(lesson_title)
    if lesson_exercise in lst:
        lst.remove(lesson_exercise)
    return lst


def swap(lesson_1, lesson_2, lst):
    lesson_1_exercise = f'{lesson_1}-Exercise'
    lesson_2_exercise = f'{lesson_2}-Exercise'
    if lesson_1 in lst and lesson_2 in lst:
        first_index = lst.index(lesson_1)
        second_index = lst.index(lesson_2)
        lst[first_index] = lesson_2
        lst[second_index] = lesson_1
        if lesson_1_exercise in lst:
            if second_index < len(lst):
                lst.remove(lesson_1_exercise)
                lst.insert(second_index + 1, lesson_1_exercise)
            else:
                lst.remove(lesson_1_exercise)
                lst.append(lesson_1_exercise)
        if lesson_2_exercise in lst:
            if second_index < len(lst):
                lst.remove(lesson_2_exercise)
                lst.insert(first_index + 1, lesson_2_exercise)
            else:
                lst.remove(lesson_2_exercise)
                lst.append(lesson_2_exercise)

    return lst


def exercise(lesson_title, sequence):
    lesson_exercise = f'{lesson_title}-Exercise'
    if lesson_title in sequence and lesson_exercise not in sequence:
        index = sequence.index(lesson_title)
        if index < len(sequence):
            sequence.insert(index + 1, lesson_exercise)
        else:
            sequence.append(lesson_exercise)
    elif lesson_title not in sequence and lesson_exercise not in sequence:
        sequence.append(lesson_title)
        sequence.append(lesson_exercise)
    return sequence


sequence = input().split(", ")

while True:

    command = input().split(":")

    if command[0] == "course start":
        break

    if command[0] == "Add":
        sequence = add(command[1], sequence)



    elif command[0] == "Insert":
        sequence = insert(command[1], int(command[2]), sequence)



    elif command[0] == "Remove":
        while command[1] in sequence:
            sequence = remove(command[1], sequence)



    elif command[0] == "Swap":
        sequence = swap(command[1], command[2], sequence)



    elif command[0] == "Exercise":
        sequence = exercise(command[1], sequence)

for i in range(1, len(sequence) + 1):
    print(f'{i}.{sequence[i - 1]}')
