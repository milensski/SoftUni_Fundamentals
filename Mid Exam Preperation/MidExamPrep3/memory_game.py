sequence = input().split()
turn = 0
while True:

    move = input().split()

    if move[0] == "end":
        print("Sorry you lose :(")
        print(' '.join(sequence))
        break

    index_1 = int(move[0])
    index_2 = int(move[1])

    turn += 1

    if 0 > index_1 or index_1 >= len(sequence) or 0 > index_2 or index_2 >= len(sequence) or index_1 == index_2:
        middle = int(len(sequence) / 2)
        sequence.insert(middle, f'-{turn}a')
        sequence.insert(middle, f'-{turn}a')
        print("Invalid input! Adding additional elements to the board")
        continue

    elif sequence[index_1] != sequence[index_2]:
        print("Try again!")

    if sequence[index_1] == sequence[index_2]:
        element = sequence[index_1]
        sequence[index_1] = "None"
        sequence[index_2] = "None"
        while "None" in sequence:
            sequence.remove("None")
        print(f"Congrats! You have found matching elements - {element}!")

    if len(sequence) <= 0:
        print(f"You have won in {turn} turns!")
        break
