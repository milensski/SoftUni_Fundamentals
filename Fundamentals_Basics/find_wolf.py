
text = input()

lst = text.split(", ")

wolf_position = lst.index("wolf") + 1

sheep_total = lst.count("sheep")

sheep_count = 0

if wolf_position == len(lst):
    print("Please go away and stop eating my sheep")
    exit()
else:
    for position in range(len(lst), 0, -1):
        if position == wolf_position:
            print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
            exit()
        else:
            sheep_count += 1