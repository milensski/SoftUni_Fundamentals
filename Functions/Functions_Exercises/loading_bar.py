def loading_bar(value):
    numbers = value // 10

    left_side = ["%" for _ in range(1, numbers + 1)]
    right_side = ['.' for _ in range(1, 11 - numbers)]

    if value == 100:
        print("100% Complete!")
        print("[", end="")
        print(*left_side, *right_side, sep='', end='')
        print("]", end="")
    else:
        print(f"{value}%", end=' ')
        print("[", end="")
        print(*left_side, *right_side, sep='', end='')
        print("]", end="\n")
        print("Still loading...")


progress = int(input())

loading_bar(progress)
